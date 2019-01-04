# gets data of states and puts them in individual lists
def getState():
  amount = int(input("how many states are in your list? "))
  i = 0
  stateAbb = []
  statePop = []
  while i < amount:
    abb = input("Enter state abbreviation: ")
    pop = int(input("Enter state Population: "))
    stateAbb.append(abb)
    statePop.append(pop)
    i = i + 1 
  return stateAbb,statePop
  print(stateAbb,statePop)



#finds populaton of state indicated by user
def searchState(stateAbb,statePop,state):
    for i in range(len(stateAbb)):
      #if the state is in the list
        if state == stateAbb[i]:
            return statePop[i]
    #if the state searched for is not in the list
    if state != stateAbb[i]:
      print("That is not a valid state abbreviation")
  

    
 # finds the population greater than the maximum the user states   
def highPopStates(stateAbb,statePop,maximum):
    counter = 0
    for i in range(len(statePop)):
      #if the state population is greater than the maximum the user states
        if statePop[i] > maximum:
            print (stateAbb[i])
            counter = counter + 1
    #if none of the states are higher than maximum
    if counter == 0:
      print(" No States are higher than the maximum sorry!")
     
  



# runs all the functions
def main():
  #initialize the lists
    stateAbb = []
    statePop = []
    #call get state
    stateAbb,statePop = getState()
    # ask user to enter state that the population needs to be found for
    state = input("Enter a state to find the population of: ")
    #call search state function
    search = searchState(stateAbb,statePop,state)
    print("The population of",state,"is", search)
    #ask the user for maximum population
    maximum = int(input("Find all the states with a population higher than: " ))
    print("The following states have populations greater than",maximum)
    #call high population state function
    statep = highPopStates(stateAbb,statePop,maximum)
