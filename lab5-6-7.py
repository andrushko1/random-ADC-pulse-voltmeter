import sys

from matplotlib import pyplot as plt
from numpy import random
from time import time
from tabulate import tabulate
# l5_d_nums -- means lab5_discrete_numbers
# l5_n_nums -- means lab5_normalized_numbers
# l5_u_nums -- means lab5_even_distribution_numbers


# tabulate headers, on discrete must be True
def tab_h(b=False):
    if b:
        return ['Discrete', 'Normalized', 'Average of 3']
    return ['Even', 'Normalized', 'Average of 3']


class Main:
    def __init__(self, var):
        self.devices = var * 3 + 10 if var < 10 else var * 2
        self.numbers = 23 + var * 10
        self.plot_recipe = self.devices_plot()

        # FOR 5
        self.l5_d_nums = self.gen_nums(self.numbers, 3)
        self.l5_d_counts = self.counter(self.l5_d_nums)
        self.l5_dn_nums = self.norm_nums(self.l5_d_nums)
        self.l5_dn_counts = self.counter(self.l5_dn_nums)

        self.l5_u_nums = self.gen_nums(self.numbers, 3, True)
        self.l5_u_counts = self.counter(self.l5_u_nums, True, id_=5)
        self.l5_nu_nums = self.norm_nums(self.l5_u_nums)
        self.l5_nu_counts = self.counter(self.l5_nu_nums)
        # FOR 6
        self.l6_d_nums = self.gen_nums(self.numbers, 5)
        self.l6_d_counts = self.counter(self.l6_d_nums)
        self.l6_dn_nums = self.norm_nums(self.l6_d_nums)
        self.l6_dn_counts = self.counter( self.l6_dn_nums)

        self.l6_u_nums = self.gen_nums(self.numbers, 5, True)
        self.l6_u_counts = self.counter(self.l6_u_nums, True, id_=6)
        self.l6_nu_nums = self.norm_nums(self.l6_u_nums)
        self.l6_nu_counts = self.counter(self.l6_nu_nums)
        # FOR 7
        self.l7_d_nums = self.gen_nums(self.numbers, 4)
        self.l7_d_counts = self.counter(self.l7_d_nums)
        self.l7_dn_nums = self.norm_nums(self.l7_d_nums)
        self.l7_dn_counts = self.counter(self.l7_dn_nums)

        self.l7_u_nums = self.gen_nums(self.numbers, 4, True)
        self.l7_u_counts = self.counter(self.l7_u_nums, True, id_=7)
        self.l7_nu_nums = self.norm_nums(self.l7_u_nums)
        self.l7_nu_counts = self.counter(self.l7_nu_nums)

        self.l7_dn_aver_lst = self.lab7_aver_nums()
        self.l7_dn_aver_counts = self.counter(self.l7_dn_aver_lst)
        self.l7_nu_aver_lst = self.lab7_aver_nums(True)
        self.l7_nu_aver_counts = self.counter(self.l7_nu_aver_lst)

    def devices_plot(self, left_border=-1.):
        one_part = 1.999 / self.devices
        border = left_border
        full_range = []
        for i in range(self.devices):
            prev = border + 0.001
            border += one_part
            full_range.append([float('%.3f' % prev), float('%.3f' % border)])
        return full_range

    def counter(self, nums_lst, check=False, id_=0):
        counts_lst = [0 for _ in range(len(self.plot_recipe))]
        for elem in nums_lst:
            for d_ranges in self.plot_recipe:
                if d_ranges[0] <= elem <= d_ranges[1]:
                    counts_lst[self.plot_recipe.index(d_ranges)] += 1
        if check:
            print('POTENTIAL COUNTERS', counts_lst)
            sum_lst = sum(counts_lst)
            p = [counts_lst[i] / sum_lst * 100 for i in range(len(counts_lst))]
            diff = max(p) - min(p)
            print('Next analyses', diff)
            if diff >= 5:
                print('BAD')
                print('numbers', sum_lst)
                double_nums = sum_lst * 2
                print('double numbers', double_nums)
                new_nums_lst = self.gen_nums(double_nums, 0, True)
                self.nums_changing(new_nums_lst, id_)

                new_nums_counts = self.counter(new_nums_lst, True, id_)
                return new_nums_counts
            else:
                print('PASSED')

        return counts_lst

    def nums_changing(self, new_nums_lst, id_):
        if id_ == 5:
            self.l5_u_nums = new_nums_lst
        elif id_ == 6:
            self.l6_u_nums = new_nums_lst
        else:
            self.l7_u_nums = new_nums_lst

    @staticmethod
    def gen_nums(nums, gens_amount, uni=False):
        nums_lst = []
        for num_id in range(nums):
            if uni == 1:
                gens_output = random.uniform(-0.999, 0.999, nums)
                return [float(f'{i:.3f}') for i in gens_output]
            else:
                gens_output = [float('%.3f' % random.uniform(-0.999, 0.999)) for _ in range(gens_amount)]
            #print(gens_output)
            for elem_id in range(gens_amount-1):
                if elem_id % 2 == 0:
                    gens_output.pop(gens_output.index(min(gens_output)))
                else:
                    gens_output.pop(gens_output.index(max(gens_output)))
                #print(gens_output)
            nums_lst.append(gens_output[0])
        return nums_lst

    @staticmethod
    def norm_nums(nums_lst):
        #val_min = min(nums_lst)
        val_max = max(nums_lst)
        sum_lst = sum(nums_lst)
        #return [float(f'{i / val_max:.3f}') for i in nums_lst]
        #lst = normalize([nums_lst], norm='l1')
        #return lst[0]
        #return [float(f'{i * sum_lst:.3f}') for i in nums_lst]
        return [float(f'{i * 0.3:.3f}') for i in nums_lst]
        #return [(float(i)-val_min)/(val_max-val_min) for i in nums_lst]

    def lab7_aver_nums(self, uni=False):
        average = []
        for i in range(len(self.l5_d_nums)):
            if uni:
                values = [self.l5_nu_nums[i], self.l6_nu_nums[i], self.l7_nu_nums[i]]
            else:
                values = [self.l5_dn_nums[i], self.l6_dn_nums[i], self.l7_dn_nums[i]]
            # print(values)
            for ii in range(len(values) - 1):
                # even gen_elem
                if ii % 2 == 0:
                    values.pop(values.index(min(values)))
                else:
                    values.pop(values.index(max(values)))
            average.append(values[0])
            # print(values[0])
        return average


if __name__ == '__main__':
    start_time = time()
    lab = Main(1)
    print(lab.devices, lab.numbers)
    print(lab.plot_recipe)
    print('L5', lab.l5_u_counts)
    print('L6', lab.l6_u_counts)
    print('L7', lab.l7_u_counts)
    #print(lab.l5_d_nums)
    #print(lab.l6_d_nums)

    # Output with tabulate lib
    table = zip(lab.l5_d_counts, lab.l5_dn_counts)
    print("\nLab 5 - Discrete Distribution\n", tabulate(table, headers=tab_h(True)))
    print(sum(lab.l5_d_counts), sum(lab.l5_dn_counts))

    table = zip(lab.l5_u_counts, lab.l5_nu_counts)
    print("\nLab 5 - Even Distribution\n", tabulate(table, headers=tab_h()))
    print(sum(lab.l5_u_counts), sum(lab.l5_nu_counts))

    table = zip(lab.l6_d_counts, lab.l6_dn_counts)
    print("\nLab 6 - Discrete Distribution\n", tabulate(table, headers=tab_h(True)))
    print(sum(lab.l6_d_counts), sum(lab.l6_dn_counts))

    table = zip(lab.l6_u_counts, lab.l6_nu_counts)
    print("\nLab 6 - Even Distribution\n", tabulate(table, headers=tab_h()))
    print(sum(lab.l6_u_counts), sum(lab.l6_nu_counts))

    table = zip(lab.l7_d_counts, lab.l7_dn_counts, lab.l7_dn_aver_counts)
    print("\nLab7 - Discrete Distribution\n", tabulate(table, headers=tab_h(True)))
    print(sum(lab.l7_d_counts), sum(lab.l7_dn_counts))

    table = zip(lab.l7_u_counts, lab.l7_nu_counts, lab.l7_nu_aver_counts)
    print("\nLab 7 - Even Distribution\n", tabulate(table, headers=tab_h()))
    print(sum(lab.l7_u_counts), sum(lab.l7_nu_counts))

    print("--- %d seconds ---" % (time() - start_time))
    print("---size: %d bytes ---" % sys.getsizeof(lab))
    # plt section
    n_bins = lab.devices
    fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(nrows=3, ncols=2)
    # Pointers
    lab5_d_data = [lab.l5_d_nums, lab.l5_dn_nums]
    lab5_u_data = [lab.l5_u_nums, lab.l5_nu_nums]
    lab6_d_data = [lab.l6_d_nums, lab.l6_dn_nums]
    lab6_u_data = [lab.l6_u_nums, lab.l6_nu_nums]
    lab7_d_data = [lab.l7_d_nums, lab.l7_dn_nums, lab.l7_dn_aver_lst]
    lab7_u_data = [lab.l7_u_nums, lab.l7_nu_nums, lab.l7_nu_aver_lst]
    # plt
    n_label = ['Вхідні', 'Вихідні', 'Середнє 3-х']
    colors = ['royalblue', 'mediumslateblue']
    # Lab5 discrete data
    ax0.hist(lab5_d_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax0.set_title('Лабораторна 5 - Дискретний')
    ax0.legend(n_label)
    # Lab5 even data
    ax1.hist(lab5_u_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax1.set_title('Лабораторна 5 - Рівномірний')
    ax1.legend(n_label)
    # Lab6 discrete data
    ax2.hist(lab6_d_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax2.set_title('Лабораторна 6 - Дискретний')
    ax2.legend(n_label)
    # Lab6 even data
    ax3.hist(lab6_u_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax3.set_title('Лабораторна 6 - Рівномірний')
    ax3.legend(n_label)
    colors.append('hotpink')
    # Lab7 discrete data
    ax4.hist(lab7_d_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax4.set_title('Лабораторна 7 - Дискретний')
    ax4.legend(n_label)
    # Lab7 even data
    ax5.hist(lab7_u_data, bins=n_bins, stacked=True, edgecolor='black', color=colors)
    ax5.set_title('Лабораторна 7 - Рівномірний')
    ax5.legend(n_label)

    plt.show()


