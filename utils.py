import numpy as np


def getClickCurve(phase, userType, x_values):
    if(phase == 0):
        # High interest / No competitors
        if(userType == 0):
            return 12700 * np.log(x_values/ 27 + 1)
        elif(userType == 1):
            return 14500 * np.log(x_values/ 20 + 1)
        else:
            return 11500 * (1 - np.exp((-1 * x_values) / 40)) + 2000 * np.log(x_values/ 35 + 1)
    elif(phase == 1):
        # Low interest / No competitors
        if(userType == 0):
            return 5700 * np.log(x_values/ 27 + 1)
        elif(userType == 1):
            return 6500 * np.log(x_values/ 20 + 1)
        else:
            return 4500 * (1 - np.exp((-1 * x_values) / 40)) + 1500 * np.log(x_values/ 35 + 1)
    elif (phase == 2):
        # Low interest / With competitors
        if(userType == 0):
            return -13500 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(70, 2.))) + 13500
        elif(userType == 1):
            return -14000 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(50, 2.))) + 14000
        else:
            return -11500 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(90, 2.))) + 11500
    else:
        # High interest / With competitors
        if (userType == 0):
            return -21500 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(55, 2.))) + 21500
        elif (userType == 1):
            return -35000 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(65, 2.))) + 35000
        else:
            return -11500 * np.exp(-np.power(x_values- 0, 2.) / (2 * np.power(35, 2.))) + 11500


def getProbabilities(userType):
    if userType == 0:
        return 0.3
    elif userType == 1:
        return 0.5
    elif userType == 2:
        return 0.2
    else:
        return 1


def smoothen_curve(curve, smoothing_window_size=800):
    smooth_curve = np.zeros(len(curve))
    for i in range(len(curve)):
        smooth_curve[i] = np.mean(curve[max(0, int(i - smoothing_window_size / 2)):
                                                    min(len(curve), int(i + smoothing_window_size / 2))])
    return smooth_curve


def demand(y,x):
    return getDemandCurve(y, x)  # aggregated fn




def getDemandCurve(userType, t):
    if (userType == 0):
        return 0.75*np.exp(-np.power(t - 200, 2.) / (2 * np.power(90, 2.))) + 0.3*np.exp(-np.power(t - 60, 2.) / (2 * np.power(60, 2.)))
    elif (userType == 1):
        return 0.75*np.exp(-np.power(t - 250, 2.) / (2 * np.power(90, 2.))) + 0.55*np.exp(-np.power(t - 65, 2.) / (2 * np.power(90, 2.)))
    elif  (userType == 2):
        return 0.42*np.exp(-np.power(t - 180, 2.) / (2 * np.power(90, 2.))) + 0.35*np.exp(-np.power(t - 85, 2.) / (2 * np.power(120, 2.)))
    else:
        return getProbabilities(0)*getDemandCurve(0,t) + getProbabilities(1)*getDemandCurve(1,t) + getProbabilities(2)*getDemandCurve(2,t)
        #return (0.75*np.exp(-np.power(t - 200, 2.) / (2 * np.power(90, 2.))) + 0.3*np.exp(-np.power(t - 60, 2.) / (2 * np.power(60, 2.))) + 0.75*np.exp(-np.power(t - 250, 2.) / (2 * np.power(90, 2.))) + 0.55*np.exp(-np.power(t - 65, 2.) / (2 * np.power(90, 2.))) + 0.42*np.exp(-np.power(t - 180, 2.) / (2 * np.power(90, 2.))) + 0.35*np.exp(-np.power(t - 85, 2.) / (2 * np.power(120, 2.)))) / 3