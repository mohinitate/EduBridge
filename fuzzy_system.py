import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# -----------------------------
# INPUT VARIABLES
# -----------------------------

communication = ctrl.Antecedent(
    np.arange(0, 11, 1), "communication"
)

teaching = ctrl.Antecedent(
    np.arange(0, 11, 1), "teaching"
)

comfort = ctrl.Antecedent(
    np.arange(0, 11, 1), "comfort"
)

participation = ctrl.Antecedent(
    np.arange(0, 11, 1), "participation"
)

atmosphere = ctrl.Antecedent(
    np.arange(0, 11, 1), "atmosphere"
)


# -----------------------------
# OUTPUT VARIABLE
# -----------------------------

environment = ctrl.Consequent(
    np.arange(0, 101, 1), "environment"
)


# -----------------------------
# MEMBERSHIP FUNCTIONS
# -----------------------------

for variable in [
    communication,
    teaching,
    comfort,
    participation,
    atmosphere
]:
    variable["low"] = fuzz.trimf(
        variable.universe, [0, 0, 5]
    )

    variable["medium"] = fuzz.trimf(
        variable.universe, [2, 5, 8]
    )

    variable["high"] = fuzz.trimf(
        variable.universe, [5, 10, 10]
    )


environment["poor"] = fuzz.trimf(
    environment.universe, [0, 0, 40]
)

environment["moderate"] = fuzz.trimf(
    environment.universe, [25, 50, 70]
)

environment["good"] = fuzz.trimf(
    environment.universe, [55, 75, 90]
)

environment["excellent"] = fuzz.trimf(
    environment.universe, [75, 100, 100]
)


# -----------------------------
# FUZZY RULES
# -----------------------------

rule1 = ctrl.Rule(
    communication["high"]
    & teaching["high"]
    & comfort["high"],
    environment["excellent"]
)

rule2 = ctrl.Rule(
    communication["high"]
    & teaching["high"]
    & participation["high"],
    environment["good"]
)

rule3 = ctrl.Rule(
    comfort["medium"]
    & participation["medium"]
    & atmosphere["medium"],
    environment["moderate"]
)

rule4 = ctrl.Rule(
    communication["low"]
    | teaching["low"],
    environment["poor"]
)

rule5 = ctrl.Rule(
    participation["low"]
    & atmosphere["low"],
    environment["poor"]
)

rule6 = ctrl.Rule(
    communication["medium"]
    & teaching["medium"]
    & comfort["high"]
    & atmosphere["high"],
    environment["good"]
)


# -----------------------------
# CONTROL SYSTEM
# -----------------------------

environment_control = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6
])


# -----------------------------
# MAIN FUZZY FUNCTION
# -----------------------------

def calculate_environment_score(
    communication_score,
    teaching_score,
    comfort_score,
    participation_score,
    atmosphere_score
):

    simulation = ctrl.ControlSystemSimulation(
        environment_control
    )

    simulation.input["communication"] = communication_score
    simulation.input["teaching"] = teaching_score
    simulation.input["comfort"] = comfort_score
    simulation.input["participation"] = participation_score
    simulation.input["atmosphere"] = atmosphere_score

    simulation.compute()

    return round(
        simulation.output["environment"],
        2
    )