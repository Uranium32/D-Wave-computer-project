from subprocess import check_call, CalledProcessError

def findSolution(lpFile, solutionFile):
    '''
     Launch the command in windows shell to find the solution of the lp file

     :param lpFile: 
     :param solutionFile:

     :type lpFile:
     :type solutionFile:

     :return solutionFile: the file of the solution
    '''
    try:
        check_call(["glpsol", "--cpxlp", lpFile , "-o", solutionFile])
    except CalledProcessError:
        print("\n/!\ Impossible de lancer la commande pour résoudre le fichier lp /!\ \n")
        exit()
    
    return solutionFile

if __name__ == "__main__":
    findSolution("test4", "soltion8")