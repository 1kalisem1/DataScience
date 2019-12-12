import matplotlib.pyplot as plt

#Graph 1/4
plt.title("Smoking Habits in 20 States\n\nPercent Who Smoke Every Day")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [6.9,15.3,15,24.9,17.7,17.7,16.9,18.5,12.6,13,23.5,8.5,7.9,10.1,12.8,15.5,13.4,19.7,18.2,14.7], "or")
plt.ylabel("Percent of daily smokers")
plt.axis([1, 20, 0, 100])
plt.show()

#Graph 2/4
plt.title("Smoking Habits in 20 States\n\nPercent Who Smoke Some Days")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [2.7,5.4,6.2,3.7,5.7,5.6,4.8,4.6,5.1,6.4,4.6,3,5.2,5.2,5,4.6,4.9,5.7,5.6,4.6], "ob")
plt.ylabel("Percent")
plt.axis([1, 20, 0, 100])
plt.show()

#Graph 3/4
plt.title("Smoking Habits in 20 States\n\nPercent of Former Smokers")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [12.6,28.3,26,23.7,20.1,22.4,26.7,24.3,22,20.7,24.7,16,16.9,16.8,25.5,25.4,25.2,23.9,25.1,25.2], "og")
plt.ylabel("Percent")
plt.axis([1, 20, 0, 100])
plt.show()

#Graph 4/4
plt.title("Smoking Habits in 20 States\n\nPercent Who Have Never Smoked")
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [77.8,50.9,52.8,47.6,56.4,54.3,51.6,52.2,60.3,60,47.1,72.5,70,67.9,55.3,54.4,55.4,50.8,51.1,55.5], "oy")
plt.ylabel("Percent")
plt.axis([1, 20, 0, 100])
plt.show()
