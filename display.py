class Display():

    def __init__(self):

        self._tries = 4

    def display_parachute(self):
        stages = [  # #dead
            """
                    
                     X
                    /|\\
                    / \\
                        
            """,
            # Fourth Stage: lost the ropes of the parachute
            """
                        
                    \ /
                     O
                    /|\\
                    / \\
            
            """,
            # Third Stage: Lost the parachute.
            """
                    \   /
                     \ /
                      O
                     /|\\
                     / \\
            """,
            # second stage, lost the top of the parachute
            """

                    /___\\
                    \\   /
                     \\ /
                      O
                     /|\\
                     / \\
            """,
            # Initial stage
            """
                     ___
                    /___\\
                    \   /
                     \ /
                      O
                     /|\\
                     / \\
            """
        ]
        return stages[self._tries]
