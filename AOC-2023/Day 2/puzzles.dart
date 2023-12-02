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
  
}

void puzzleTwo(List<String> input) {
  
}

void main() {
  List<String> input = readFile();
  puzzleOne(input);

  // puzzleTwo(input);
}