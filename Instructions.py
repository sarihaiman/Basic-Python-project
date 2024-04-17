import pygame
pygame.init()

class Instructions:

    def instructions(self,nameofcake):
        """A function that speaks to the user the instructions for preparing the cake of his choice"""
        mp3_end = "./voice/coffee/end.mp3"
        if nameofcake == "coffee":
            mp3_file1 = "./voice/coffee/1.mp3"
            mp3_file2 = "./voice/coffee/2.mp3"
            mp3_file3 = "./voice/coffee/3.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_file1)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continued: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load(mp3_file2)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continued: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.init()
                            pygame.mixer.music.load(mp3_file3)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continued: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(mp3_end)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'e' to exist: ")
                                        if user_input.lower() == 'e':
                                            pygame.mixer.music.stop()
                                            break
        if nameofcake == "coconut":
            mp3_file4 = "./voice/coconut/4.mp3"
            mp3_file5 = "./voice/coconut/5.mp3"
            mp3_file6 = "./voice/coconut/6.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_file4)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continued: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load(mp3_file5)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continued: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.init()
                            pygame.mixer.music.load(mp3_file6)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continued: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(mp3_end)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'e' to exist: ")
                                        if user_input.lower() == 'e':
                                            pygame.mixer.music.stop()
                                            break
        if nameofcake == "apple":
            mp3_file7 = "./voice/apple/7.mp3"
            mp3_file8 = "./voice/apple/8.mp3"
            mp3_file9 = "./voice/apple/9.mp3"
            mp3_file10 = "./voice/apple/10.mp3"
            mp3_file11 = "./voice/apple/11.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_file7)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continued: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load(mp3_file8)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continued: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.init()
                            pygame.mixer.music.load(mp3_file9)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continued: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(mp3_file10)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'c' to continued: ")
                                        if user_input.lower() == 'c':
                                            pygame.mixer.music.stop()
                                            pygame.mixer.init()
                                            pygame.mixer.music.load(mp3_file11)
                                            pygame.mixer.music.play(loops=-1)
                                            while pygame.mixer.music.get_busy():
                                                user_input = input("Press 'c' to continued: ")
                                                if user_input.lower() == 'c':
                                                    pygame.mixer.music.stop()
                                                    pygame.mixer.init()
                                                    pygame.mixer.music.load(mp3_end)
                                                    pygame.mixer.music.play(loops=-1)
                                                    while pygame.mixer.music.get_busy():
                                                        user_input = input("Press 'e' to exist: ")
                                                        if user_input.lower() == 'e':
                                                            pygame.mixer.music.stop()
                                                            break



    def printimg(self,nameofcake):
        """The function shows the picture of the requested cake"""
        if nameofcake == "coffee":
            pygame.init()
            X = 560
            Y = 370
            scrn = pygame.display.set_mode((X, Y))
            pygame.display.set_caption('image')
            imp = pygame.image.load("./7.jpg").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.flip()
            status = True
            while (status):
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        status = False
            pygame.quit()
        if nameofcake == "coconut":
            X = 560
            Y = 370
            scrn = pygame.display.set_mode((X, Y))
            pygame.display.set_caption('image')
            imp = pygame.image.load("./8.jpg").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.flip()
            status = True
            while (status):
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        status = False
            pygame.quit()
        if nameofcake == "apple":
            X = 560
            Y = 370
            scrn = pygame.display.set_mode((X, Y))
            pygame.display.set_caption('image')
            imp = pygame.image.load("./9.jpg").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.flip()
            status = True
            while (status):
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        status = False
            pygame.quit()
