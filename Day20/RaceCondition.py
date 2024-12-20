def main():
 
    fileName = "test.txt"
    path = "../../Advent Of Code Cases/Day20/" + fileName

    raceTrack = []
    with open(path, 'r') as file:
        for line in file:
            raceTrack.append(line)

    print(raceTrack)
        
if __name__ == "__main__":
    main()
