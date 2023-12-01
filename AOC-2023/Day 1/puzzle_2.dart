import 'dart:async';
import 'dart:io';
import 'dart:convert';

List readFile() {
  List<dynamic> lines = [];
  var path = "input.txt";

  lines = new File(path).readAsLinesSync();

  return lines;
}

int? tryParse(String input) {
  String source = input.trim();
  return int.tryParse(source);
}

Map<String, int> numStrs = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
};

main() {
  List<dynamic> lines = readFile();

  int sum = 0;
  List<int> nums = [];
  
  for(String item in lines) {
    for(int i = 0; i < item.length; i++) {
      int? result = tryParse(item[i]);
      if(result != null) {
        nums.add(result);
        
      } else {
        for(String numStr in numStrs.keys.toList()) {
          if(i+numStr.length > item.length) {
            continue;
          } else {
            String substr = item.substring(i, i+numStr.length);
              if(substr == numStr) {
                nums.add(numStrs[substr]!);
              }
          }
        }
      }
    }

    if(nums.length == 1) {
      int numToAdd = int.parse("${nums[0]}${nums[0]}");
      print(numToAdd);
      sum += numToAdd;
    } else {
      int numToAdd = int.parse("${nums[0]}${nums[nums.length-1]}");
      print(numToAdd);
      sum += numToAdd;
    }
    nums.clear();
  }

  print(sum);
}