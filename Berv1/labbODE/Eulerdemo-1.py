#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import mplDeprecation
from matplotlib.widgets import Button, TextBox
import scipy.integrate as ode
from math import pi
import warnings

print("-----------------------------------------------------")
print("Euler's method for the non-linear ODE")
print("     dy/dt = cos(y*t), 0 < t < 2*pi,")
print("     y(0) = 0.")
print("-----------------------------------------------------")
print("This demo program solves the non-linear ODE using Euler's method. For comparison the exact solution is plotted in the figure (not really exact, a highly accurate method from SciPy is used). Use the program as follows:")
print("1. Choose a step size, type in the textbox.")
print("2. Press \"Initialize\" to initialize Euler's method.")
print("3. Press \"Step once\" to perform one iteration, continue until the final time is reached. Pay attention to the difference between exact and approximate solution.")
print("4. Press \"Reset\" to reset the solver and try another step size. Quit the program by closing the figure window.")
print("-----------------------------------------------------")

# Hide warning "Toggling axes navigation from the keyboard is deprecated..." when typing in textbox. 
warnings.filterwarnings("ignore",category=mplDeprecation)

# RHS function
def f(t,y):
    return np.cos(y*t)

# Set ODE parameters
maxintervals = 50
tspan = (0,2*pi)
y0 = 0

# Setup the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_navigate(False)
plt.title('Euler\'s method')

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.10, bottom=0.20)

# Draw the initial plot. The 'line' variable is used for modifying the interval line later.
# Plot exact solution using SciPys RK45
SOL = ode.solve_ivp(f, tspan, np.array([y0]), method='RK45', rtol=1e-10, atol=1e-10)
ax.plot(SOL.t,SOL.y[0],label='Exact solution',color='blue')
[line] = ax.plot(tspan[0],y0,'r*-',label='Approximate solution');
plt.xlabel('$t$')
plt.ylabel('$y$')
ax.legend()
line.set_visible(False)
ax.set_xlim([0,7])
ax.set_ylim([0, 1.5])

# Define textbox and buttons
reset_button_ax = fig.add_axes([0.60, 0.03, 0.1, 0.04])
reset_button_ax.set_navigate(False)
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')
reset_button_ax.set_navigate(False)

textbox_ax = fig.add_axes([0.20, 0.03, 0.1, 0.04])
textbox_ax.set_navigate(False)
textbox = TextBox(textbox_ax, "Step size: ", initial='', color='.95', hovercolor='1', label_pad=0.01)
textbox_ax.set_navigate(False)

step_button_ax = fig.add_axes([0.35, 0.03, 0.2, 0.04])
step_button_ax.set_navigate(False)
step_button = Button(step_button_ax, 'Initialize', hovercolor='0.975', color='0.85')
step_button.set_active(True)

def reset_button_on_clicked(mouse_event):
    global curr_step
    textbox.set_val("")
    if not curr_step == 0:
        step_button.set_active(True)
        textbox.set_active(True)
        line.set_xdata(tspan[0])
        line.set_ydata(y0)
        line.set_visible(False)
        print("----------------------------")
        step_button.label.set_text("Initialize")
        curr_step = 0
    plt.draw()

curr_step = 0
def step_button_on_clicked(mouse_event):
    global curr_step, y, t, h, N
    # First step. Change label and show initial guess
    if curr_step == 0:
        try:
            step_button.set_active(True)

            h = float(textbox.text)
        except ValueError:
            print("Input '{:s}' could not be interpreted as a step size (float). Try again.".format(textbox.text))    
            return
    
        if not h > 0 or h > 2*pi:
            print("Step size error. Choose step size on the interval 0 < h < 2*pi. Current h: {:f}".format(h))
            return        

        line.set_visible(True)
        textbox.set_active(False)
        step_button.label.set_text("Step once")
        plt.draw()
        h = min(h,2*pi)
        t = np.arange(tspan[0],tspan[1],h)
        N = t.size

        print("Running Euler's method with step size: {:f}. Press 'Step once' to iterate.".format(h))
        y = np.zeros(N)
        y[0] = y0
        curr_step += 1


    elif curr_step == N: # Final step. Inactivate step button, get final solution and error (step again with smaller h if needed).
        step_button.set_active(False)
        yfinal = y[curr_step-1]

        if not tspan[1] == t[-1]:
            hfinal = tspan[1] - t[-1]
            yfinal = y[curr_step-1] + hfinal*f(t[curr_step-1],y[curr_step-1])
            t = np.append(t, tspan[1])
            y = np.append(y, yfinal)
            line.set_xdata(t)
            line.set_ydata(y)
            plt.draw()
    
        err = abs(y[curr_step] - SOL.y[0][-1])
        print("Final time reached. Error: {:e}".format(err))
    else:    
        y[curr_step] = y[curr_step-1] + h*f(t[curr_step-1],y[curr_step-1])
        line.set_xdata(t[:curr_step+1])
        line.set_ydata(y[:curr_step+1])
        plt.draw()
        curr_step += 1

reset_button.on_clicked(reset_button_on_clicked)
step_button.on_clicked(step_button_on_clicked)

plt.show()
