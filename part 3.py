starting = 1
while starting == 1:
    try:
        user =str(input('Select Staff or Student : '))

        if user.lower() == 'staff':
            #print('multiple input enabled')
            staff_mode= 'on'
            starting -= 1
        elif user.lower() == 'student':
            #print(' input once ')
            staff_mode= 'off'
            starting -= 1
    except :
        print(' hELLO tHERE Rooky :)   U CAN\'T LEAVE, Select one of above')
        



Pre_def = (00,20,40,60,80,100,120)
Result_list = []
X =  ''



Progress  = 0
Exclude   = 0
Trailer   = 0
Retriever = 0

def RESET():
    global Pass_add
    Pass_add    = ''
    global Defer_add
    Defer_add   = ''
    global Fail_add
    Fail_add    = ''

    global pass_x
    pass_x=0
    global defer_x
    defer_x=0
    global fail_x
    fail_x=0

    global result
    result = ''
    

RESET()

if staff_mode == 'on':
    print('\nStaff Version with Histogram\n\nInsert following integers only',Pre_def)

def check_appen_list():
    if  (pass_x and defer_x and fail_x) == 1:  # make sure not to return progression values for wrong inputs
        X = result, Pass_add, Defer_add, Fail_add
        Result_list.append(X)


page_break = '_______________________________________________________________________'

input_count = 1
while input_count==1:
    if staff_mode == 'on':
        Prg_run = str(input("\nPress any key to continue or \'q\' to quit and see results \n Would you like to continue : "))
        Total = Progress + Exclude + Trailer + Retriever
    

    check_appen_list()
        
       
    if staff_mode == 'on':
        if Prg_run.lower() == 'q' :
            print('\n================================\n  End of the the Results Input \n')
            input_count = 0
            break

    while input_count==1:
      
        print()
        try:
            #input_count-=1
            
            
            if 1==1 : #always true   # CONTINUE PART
                Pass  = int(input('Enter your Pass credits  : '))
                if ( Pass in Pre_def ):
                    Pass_add = Pass
                    pass_x=1
                    x=1
                else:
                    RESET()
                    print('out of range ')
                    continue
            

                Defer = int(input('Enter your Defer credits : '))
                if ( Defer in Pre_def ):
                    Defer_add = Defer
                    defer_x=1
                    x=1
                else:
                    RESET()
                    print('out of range ')
                    continue
            

                Fail  = int(input('Enter your Fail credits  : '))
                if ( Fail in Pre_def ):
                    Fail_add = Fail
                    fail_x=1
                    x=1
                else:
                    RESET()
                    print('out of range ')
                    continue
            
            


            if x == 1 :         # to make sure there's no false inputs
                if Pass + Defer + Fail == 120:
                    #print(Pass,Defer,Fail)
                    if staff_mode == 'off':     # work on student only
                        input_count -= 1

                    if Pass == 120:
                        result = 'Progress'
                        print(result)
                        Progress += 1
                        break
                    elif Fail >= 80 :
                        result = 'Exclude'
                        print(result)
                        Exclude += 1
                        break
                    elif Pass == 100:
                        result = 'Module trailer'
                        print(result)
                        Trailer += 1
                        break
                    elif Pass < 100:
                        result = 'Module retriever'
                        print(result)
                        Retriever += 1
                        break
                else:

                    RESET()
                    print('Total incorrect, not 120')

            
            
            
        except ValueError:
            RESET()
            print('Integer Required')
        


# HISTOGRAM
if staff_mode == 'on':

    # Horizontal Histogram
    print(page_break, '\n', ' Horizontal Histogram' )
    print(f"Progress  { Progress:4}  :  {Progress  * 'x ':1}")
    print(f"Trailer   {  Trailer:4}  :  {Trailer   * 'x ':1}")
    print(f"Retriever {Retriever:4}  :  {Retriever * 'x ':1}")
    print(f"Exclude   {  Exclude:4}  :  {Exclude   * 'x ':1}")

    
    print('\nTotal outcomes  : ',Total)





    # Vertical Histogram
    print(page_break, '\n', ' Vertical Histogram\n' )
    print('  Progress   Trailer   Retriever   Exclude')
    Prog = 'x'
    Exc  = 'x'
    Trail= 'x'
    Retr = 'x'

    x = (Progress,Exclude,Trailer,Retriever)
    while max(Progress,Exclude,Trailer,Retriever) >0:
        for i in x:
            
            if Progress  >0:
                Progress -= 1
            else:Prog=' '
                
            if Exclude  >0:
                Exclude  -= 1
            else:Exc=' '
            
            if Trailer  >0:
                Trailer  -= 1
            else:Trail=' '
            
            if Retriever  >0:
                Retriever -= 1
            else:Retr=' '

            well =f'     {Prog:10} {Trail:10} {Retr:10} {Exc:9}'
            print(well)
    print('\nTotal outcomes  : ',Total)




    # List
    print(page_break, '\n', ' Progression List \n' )


    for I in Result_list:
        output = f'{I[0]:17} - {I[1]:3}, {I[2]:3}, {I[3]:3}'
        print(output)
        

## part 4

#else: print('')
