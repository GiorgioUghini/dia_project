import numpy as np


def fun(t, userType, phase):
    if (userType == 0):
        if (phase == 0):
            return -16500 * np.exp(-np.power(t - 0, 2.) / (2 * np.power(50, 2.))) + 16500
        elif (phase == 1):
            return 8200 * (1 - np.exp((-1*t)/85))
        else:
            return 5500 * np.log(t/27+1)
    elif (userType == 1):
        if (phase == 0):
            return 14500 * (1 - np.exp((-1*t)/70)) + 1000 * np.log(t+1) + 1200*np.exp(-np.power(t - 10, 2.) / (2 * np.power(5, 2.)))
        elif (phase == 1):
            return -7500 * np.exp(-np.power(t - 0, 2.) / (2 * np.power(50, 2.))) + 7500
        else:
            return 6500 * np.log(t/20+1)
    else:
        if (phase == 0):
            return 5500 * (1 - np.exp((-1*t)/10))
        elif (phase == 1):
            return 4500 * (1 - np.exp((-1*t)/20)) - 1500*np.exp(-np.power(t - 80, 2.) / (2 * np.power(40, 2.))) + 200
        else:
            return 4500 * (1 - np.exp((-1*t)/40)) + 1500 * np.log(t/35+1)


class NSCMABEnvironment():
    def __init__(self, budgets_list, sigma, horizon):
        self.N_PHASES = 3
        # We hardcode N_PHASES and all the functions here because it would compromise the main code
        # to pass all these as parameters. However, it can be easily done, making the code more
        # reusable but less readable
        self.t = 0
        self.budgets = budgets_list
        self.horizon = horizon
        self.means = [fun(budgets_list[userType], userType, phase) for userType in range(0, len(budgets_list))
                      for phase in range(0, self.N_PHASES)]
        # [ FUN(0,0), FUN(0,1), FUN(0,2), ..., FUN(1,0), FUN(1,1), FUN(1,2), ...]

        self.sigma = sigma

    def round(self, pulled_arm, userType):
        phase_size = self.horizon / self.N_PHASES
        current_phase = int(self.t / phase_size)
        mean = self.means[userType * self.N_PHASES + current_phase][pulled_arm]
        # We are supposing same variance among all userTypes and phases.
        # If there are some phases with more uncertainty than others, just keep track
        # of it by instantiating self.sigma as a list based upon the current phase
        return np.random.normal(mean, self.sigma)

    def ahead(self):
        self.t += 1
        return
