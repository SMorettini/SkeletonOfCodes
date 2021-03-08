from statemachine import StateMachine

class StateMachineImplementation:
    '''
    Implementation of the specific StateMachine following the need of our project
    '''
    memory=[]
    m={}

    def __init__(self):
        self.m = StateMachine()
        #Declaration of all the states
        self.m.add_state("StateA", self.StateA_transitions)
        self.m.add_state("StateB", self.StateB_transitions)
        self.m.add_state("StateC", self.StateC_transitions)
        self.m.set_start("StateA")

    #method for evaluating the OR of a list of variables
    @staticmethod
    def conditionOr(op,data, names, values):
        result=False
        for i,key in enumerate(names):
            if(op==">"):
                result=result or abs(data[key])>values[i]
            else:
                result=result or abs(data[key])<values[i]
        return result

    #method for evaluating the AND of a list of variables
    @staticmethod
    def conditionAnd(op,data, names, values):
        result=True
        for i,key in enumerate(names):
            if(op==">"):
                result=result and abs(data[key])>values[i]
            else:
                result=result and abs(data[key])<values[i]
        return result

    #Declaration of the transition from the StateA to the other possible states
    def StateA_transitions(self, data):
        if self.conditionAnd(">",data, ["a", "v", "c","d"], [0.9, 5, 0.005, 0.8]):
            newState = "StateB"
        else:
            newState = "StateC"
        return newState

    #Declaration of the transition from the StateB to the other possible states
    def StateB_transitions(self, data):
        if (data["a"] * data["b"]) < 40:
            newState = "StateA"
        elif self.conditionAnd(">",data, ["c","d"], [15,70]):
            newState = "StateB"
        elif self.conditionAnd("<",data, ["a", "b", "c","d"], [0.9, 5, 0.005, 0.8]):
            newState = "StateC"
        else:
            newState = "StateA"
        return newState

    #Declaration of the transition from the StateC to the other possible states
    def StateC_transitions(self, data):
        newState = "StateA"
        return newState


    def runOneStep(self,data):
        return self.m.runOneStep(data)

#Code for testing the state machine
#
#if __name__== "__main__":
#    m = StateMachineSM()
#
#    m.runOneStep({"a" :0,"b" :0,"c":0, "d":0 })
#    m.runOneStep({"a" :1,"v" :1,"c":1, "d":1 })
