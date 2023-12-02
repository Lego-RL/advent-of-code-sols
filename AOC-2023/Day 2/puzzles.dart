import 'dart:async';
import 'dart:io';
import 'dart:convert';

List<String> readFile() {
  List<String> lines = [];
  var path = "input.txt";
  lines = new File(path).readAsLinesSync();
  return lines;
}

void puzzleOne(List<String> input) {
  List<int> possibleGameIDs = [];

  Map<String, int> maxVals = {
    "red": 12,
    "green": 13,
    "blue": 14,
  };

  for(String line in input) {
    bool gamePossible = true;
    var splitInfo = line.split(":");
    final String game = splitInfo[1]; //cubes picked
    int gameID = int.parse(splitInfo[0].split(" ")[1]);

    List<String> individualRolls = game.split(";");
    for(String roll in individualRolls) {
      print("roll: $roll");
      List<String> cubes = roll.split(",");

      //trim strings
      for(int i = 0; i < cubes.length; i++) {
        cubes[i] = cubes[i].trim();
      }

      for(String cube in cubes) {
        final cubeDetails = cube.split(" ");
        int numCubes = int.parse(cubeDetails[0]);
        String cubeColor = cubeDetails[1];

        if(numCubes > maxVals[cubeColor]!) {
          gamePossible = false;
          break;
        }
      }
      
    }
    if(gamePossible) {
      possibleGameIDs.add(gameID);
    }

    //reset val
    gamePossible = true;
  }

  var sum = possibleGameIDs.reduce((a, b) => a + b);
  print(sum);
}


void puzzleTwo(List<String> input) {
  int sum = 0;

    Map<String, int> largestValsIndices = {
      "red": 0,
      "green": 1,
      "blue": 2,
    };

    for(String line in input) {
      // ints represent largest red, green and blue cube num
      List<int> largestVals = [0, 0, 0];
      var splitInfo = line.split(":");
      final String game = splitInfo[1]; //cubes picked
      int gameID = int.parse(splitInfo[0].split(" ")[1]);

      List<String> individualRolls = game.split(";");
      for(String roll in individualRolls) {
        List<String> cubes = roll.split(",");

        //trim strings
        for(int i = 0; i < cubes.length; i++) {
          cubes[i] = cubes[i].trim();
        }

        for(String cube in cubes) {
          final cubeDetails = cube.split(" ");
          int numCubes = int.parse(cubeDetails[0]);
          String cubeColor = cubeDetails[1];

          int largestValsIndex = largestValsIndices[cubeColor]!;

          if(numCubes > largestVals[largestValsIndex]) {
            largestVals[largestValsIndex] = numCubes;
          }
        }
        
      }
      int powerVal = largestVals[0] * largestVals[1] * largestVals[2];
      print(powerVal);
      sum += powerVal;
    }
    print(sum);
  }

void main() {
  List<String> input = readFile();
  // puzzleOne(input);

  puzzleTwo(input);
}