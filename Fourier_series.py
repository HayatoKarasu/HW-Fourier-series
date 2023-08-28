from matplotlib import pyplot as plt

plt.text(0.01, 0.9, "Ряд фурье - это математический инструмент", fontsize=14)
plt.text(0.01, 0.8, "который позволяет разложить сложную ", fontsize=14)
plt.text(0.01, 0.7, "функцию на сумму простых функций.", fontsize=14)
plt.text(0.01, 0.6, "Расчитывается по формуле:", fontsize=14)
form = r"$\frac{a_0}{2} + \sum_{n=1}^\infty (a_n cos nx + b_n sin nx)$"
plt.text(0.01, 0.4, form, fontsize=20)
plt.text(0.01, 0.3, "где:", fontsize=14)
form = r"$a_0, a_n, b_n$"
plt.text(0.01, 0.2, form, fontsize=14)
plt.text(0.01, 0.1, "это коэффициенты ряда", fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Коэффициенты расчитываются по формулам:", fontsize=14)
form = r"$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi f(x)dx$"
plt.text(0.01, 0.7, form, fontsize=20)
form = r"$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x)cos(nx)dx$"
plt.text(0.01, 0.5, form, fontsize=20)
form = r"$b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x)sin(nx)dx$"
plt.text(0.01, 0.3, form, fontsize=20)
plt.text(0.01, 0.2, "При условии, что дана функция:", fontsize=14)
form = r"$y = f(x) с_ определением [{-\pi};\pi]$"
plt.text(0.01, 0.1, form, fontsize=20)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Так же используются период разложения:", fontsize=14)
form = r"$T = 2\pi$"
plt.text(0.01, 0.7, form, fontsize=20)
plt.text(0.01, 0.6, "и полупериод разложения:", fontsize=14)
form = r"$T = \frac{T}{2} = \pi$"
plt.text(0.01, 0.4, form, fontsize=20)
plt.text(0.01, 0.3, "Ряд Фурье имеет широкое применение", fontsize=14)
plt.text(0.01, 0.2, "в различных областях науки и техники,", fontsize=14)
plt.text(0.01, 0.1, "позволяя упростить сложные задачи.", fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()