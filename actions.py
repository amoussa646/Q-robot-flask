import robot
def action(nlu):
                intent=""
                try:
                    intent = nlu[0]['name']
                    isIntent= True
                    print("Intent : "+ intent)
                except:
                    print("no intents detected")
                    
                    
                if(intent=="move_eyes"):   
                    
                    try:  
                        value= nlu[1][0]['value']
                        if(value=="right"):
                            robot.eyesright()
                        elif(value=="left"):
                            robot.eyesleft()
                        elif(value=="up"):
                            robot.eyesup()
                        elif(value=="down"):
                            print("eyes down")
                            robot.eyesdown()
                        elif(value=="forward"):
                            print("eyes forwaaaard")
                            robot.eyesforward()
                        
                    except:
                        print("no entities detected")