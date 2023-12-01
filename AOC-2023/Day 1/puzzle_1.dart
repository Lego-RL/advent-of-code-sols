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

main() {
  List<dynamic> lines = readFile();

  int sum = 0;
  List<int> nums = [];
  
  for(String item in lines) {
    for(int i = 0; i < item.length; i++) {
      int? result = tryParse(item[i]);
      if(result != null) {
        nums.add(result);
      }
    }

    if(nums.length == 1) {
      int numToAdd = int.parse("${nums[0]}${nums[0]}");
      sum += numToAdd;
    } else {
      int numToAdd = int.parse("${nums[0]}${nums[nums.length-1]}");
      sum += numToAdd;
    }
    nums.clear();
  }

  print(sum);
}