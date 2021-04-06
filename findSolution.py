from subprocess import check_call, CalledProcessError

def findSolution(lpFile, solutionFile):
    try:
        check_call(["glpsol", "--cpxlp", lpFile, "-o", solutionFile])
    except CalledProcessError:
        print("Impossible de lancer la commande pour résoudre le fichier lp")
    
    return solutionFile

if __name__ == "__main__":
    findSolution("test4.lp", "soltion8.txt")