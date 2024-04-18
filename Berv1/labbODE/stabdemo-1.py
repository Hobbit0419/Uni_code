#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import mplDeprecation
from matplotlib.widgets import Button, TextBox
from math import ceil
import warnings

print("-----------------------------------------------------")
print("Euler's method for the non-linear ODE")
print("     dy/dt = lambda*y, 0 < t < 1,")
print("     y(0) = 0.")
print("-----------------------------------------------------")
print("This demo program solves the linear ODE using explicit and implicit Euler's method. For comparison the exact solution is plotted in the figure. Use the program as follows:")
print("1. Choose a step size and parameter lambda, type in the text boxes.")
print("2. Press \"Initialize\" to initialize the methods. The analytical solution with the chosen lambda is plotted.")
print("3. Press \"Step once\" to perform one iteration, continue until the final time is reached. Pay attention to the difference between exact and approximate solutions with explicit and implicit Euler.")
print("4. Press \"Reset\" to reset the solver and try another step size and lambda. Quit the program by closing the figure window.")
print("-----------------------------------------------------")

# Hide warning "Toggling axes navigation from the keyboard is deprecated..." when typing in textbox. 
warnings.filterwarnings("ignore",category=mplDeprecation)

# Analytical solution
def yana(t,La):
    return np.exp(La*t)

# Set ODE parameters
maxintervals = 50
tspan = (0,1)
y0 = 1

# Setup the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space
fig.subplots_adjust(left=0.10, bottom=0.25)

# Initialize plot
tt = np.linspace(tspan[0],tspan[1],1000)
[line_an] = ax.plot(tt, yana(tt,0),label='Exact solution',color='blue')
[line_ex] = ax.plot(tspan[0],y0,'r*-',label='Explicit Euler');
[line_im] = ax.plot(tspan[0],y0,'y*-',label='Implicit Euler');
plt.legend()
line_an.set_visible(False)
line_ex.set_visible(False)
line_im.set_visible(False)
plt.xlabel('$t$')
plt.ylabel('$y$')
ax.set_xlim([0,1])
ax.set_ylim([-1, 2])

# Define textboxes and buttons
reset_button_ax = fig.add_axes([0.45, 0.03, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')

textbox_h_ax = fig.add_axes([0.20, 0.1, 0.1, 0.04])
textbox_h = TextBox(textbox_h_ax, "Step size: ", initial='', color='.95', hovercolor='1', label_pad=0.01)

textbox_La_ax = fig.add_axes([0.45, 0.1, 0.1, 0.04])
textbox_La = TextBox(textbox_La_ax, "Lambda: ", initial='', color='.95', hovercolor='1', label_pad=0.01)

step_button_ax = fig.add_axes([0.10, 0.03, 0.2, 0.04])
step_button = Button(step_button_ax, 'Initialize', hovercolor='0.975', color='0.85')
step_button.set_active(True)

# Define button functions
def reset_button_on_clicked(mouse_event):
    global curr_step
    if not curr_step == 0:
        step_button.set_active(True)
        textbox_h.set_active(True)
        textbox_La.set_active(True)
        line_ex.set_xdata(tspan[0])
        line_ex.set_ydata(y0)
        line_ex.set_visible(False)
        line_im.set_xdata(tspan[0])
        line_im.set_ydata(y0)
        line_im.set_visible(False)
        line_an.set_visible(False)
        print("----------------------------")
        step_button.label.set_text("Initialize")
        curr_step = 0
    plt.draw()

curr_step = 0
def step_button_on_clicked(mouse_event):
    global curr_step, ycurr_ex, ycurr_im, tcurr, h, N, La
    if curr_step == 0:
        # Read textboxes
        try:
            h = float(textbox_h.text)
        except ValueError:
            print("Input '{:s}' could not be interpreted as a step size (float). Try again.".format(textbox_h.text))    
            return

        try:
            La = float(textbox_La.text)
        except ValueError:
            print("Input '{:s}' could not be interpreted as lambda (float). Try again.".format(textbox_La.text))    
            return

        if not h > 0 or h > 1:
            print("Step size should be on the interval 0 < h < 1, current h: {:f}. Try again.".format(h))
            return    
    
        if not La < 0:
            print("Lambda should be negative, current lambda: {:f}. Try again.".format(La))
            return        

        # Plot analytical solution
        ydata = yana(line_an.get_xdata(), La)
        line_an.set_ydata(ydata)
        ax.set_ylim([np.floor(np.min(ydata)-1),np.ceil(np.max(ydata)+1)])

        # Show curves, deactivate textboxes and change label
        line_an.set_visible(True)
        line_ex.set_visible(True)
        line_im.set_visible(True)
        textbox_h.set_active(False)
        textbox_La.set_active(False)
        step_button.label.set_text("Step once")
        
        # Set solver parameters
        tcurr = 0
        N = int(ceil(tspan[1]/h)) # number of intervals
        
        ycurr_ex = y0
        ycurr_im = y0

        print("Running Euler's methods with step size: {:f} on ODE with lambda: {:f}. Stability criterion for explicit Euler: h < {:f}. Press 'Step once' to iterate.".format(h,La,2./abs(La)))
        curr_step += 1

    elif curr_step == N:
        # Deactivate step button
        step_button.set_active(False)

        # If not at final time, do one more step and update plots
        if abs(tspan[1] - tcurr) > 1e-14:
            h = tspan[1] - tcurr
            ycurr_ex = ycurr_ex*(1 + h*La)
            ycurr_im = ycurr_im/(1 - h*La)
            tcurr += h

            line_ex.set_xdata(np.append(line_ex.get_xdata(),tcurr))
            line_ex.set_ydata(np.append(line_ex.get_ydata(),ycurr_ex))

            line_im.set_xdata(np.append(line_im.get_xdata(),tcurr))
            line_im.set_ydata(np.append(line_im.get_ydata(),ycurr_im))
    
        print("Final time t = {:f} reached.".format(tspan[1]))
    else:    
        # Do one Euler step and update plots
        ycurr_ex = ycurr_ex*(1 + h*La)
        ycurr_im = ycurr_im/(1 - h*La)
        tcurr += h

        line_ex.set_xdata(np.append(line_ex.get_xdata(),tcurr))
        line_ex.set_ydata(np.append(line_ex.get_ydata(),ycurr_ex))

        line_im.set_xdata(np.append(line_im.get_xdata(),tcurr))
        line_im.set_ydata(np.append(line_im.get_ydata(),ycurr_im))
        
        curr_step += 1

    plt.draw()

reset_button.on_clicked(reset_button_on_clicked)
step_button.on_clicked(step_button_on_clicked)

plt.show()
