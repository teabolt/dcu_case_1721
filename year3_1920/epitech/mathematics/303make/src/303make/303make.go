package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"sort"
)


var help = "USAGE\n" +
		   "\t./303make makefile [file]\n" +
		   "DESCRIPTION\n" +
		   "\tmakefile    name of the makefile\n" +
		   "\tfile        name of a recently modified file\n"


func error(s string) {
	fmt.Println(s)
	os.Exit(84)
}


// a map from target name (string) to a Target Definition struct
type DependencyMap = map[string]TargetDefinition


// target struct with a list of its prerequisites (string array) and commands to execute (string)
type TargetDefinition struct {
	prerequisites []string
	recipe string
}


type Matrix = [][]int


func readDependencyMap(filename string) DependencyMap {
	depMap := make(DependencyMap)

	file, err := os.Open(filename)
	if err != nil {
		error(fmt.Sprintf("File \"%s\" could not be opened", filename))
	}
	scanner := bufio.NewScanner(file)

	// group lines by rule
	var tabulation [][]string
	i := 0
	for scanner.Scan() {
		// keep going unless Scan returns false (in case of Error or io.EOF)
		text := scanner.Text()
		if strings.Contains(text, ":") {
			// target and prerequisites line
			// create new group
			tabulation = append(tabulation, []string{text})
		} else if len(text) != 0 {
			// recipe line
			// add to current group
			tabulation[i] = append(tabulation[i], text)
		} else {
			// newline separator between rules
			// move to next group
			i += 1
		}
	}
	if err := scanner.Err(); err != nil {
		error(fmt.Sprintf("Error reading file: %v", err))
	}
	
	// add each rule
	for _, rule := range tabulation {
		declaration := rule[0]
		sep := strings.Split(declaration, ":")
		target := sep[0]
		var prerequisites []string;
		if len(sep) == 2 {
			prerequisites = strings.Split(strings.TrimSpace(sep[1]), " ")
		} else {
			prerequisites = make([]string, 0)
		}
		recipe := strings.Join(rule[1:], "\n")
		depMap[target] = TargetDefinition{prerequisites, recipe}
	}
	return depMap
}


func getObjectIndex(depMap DependencyMap) []string {
	// read objects from targets and prerequisites
	objects := make([]string, 0, len(depMap))
	for target := range depMap {
		// add target
		objects = append(objects, target)
		// add all prerequisites
		objects = append(objects, depMap[target].prerequisites...)
	}
	
	// remove duplicates
	// to map (set)
	objects_map := make(map[string]bool)
	for _, object := range objects {
		objects_map[object] = true
	}

	// to list
	objects = make([]string, 0, len(objects_map))
	for key := range objects_map {
		objects = append(objects, key)
	}

	// sort alphabetically
	sort.Strings(objects)
	return objects
}


// create a square size*size matrix with all zeroes
func initializeMatrix(size int) Matrix {
	matrix := make(Matrix, size)
	for i := range matrix {
		matrix[i] = make([]int, size)
	}
	return matrix
}


func indexOf(array []string, value string) int {
    for i, v := range array {
        if (v == value) {
            return i
        }
    }
    return -1
}


func buildGraph(depMap DependencyMap) Matrix {
	// get index of dependencies
	objects := getObjectIndex(depMap)

	// create empty matrix
	adjacencyMatrix := initializeMatrix(len(objects))

	// create a graph
	for target := range depMap {
		colIndex := indexOf(objects, target)
		prerequisites := depMap[target].prerequisites
		for _, dep := range prerequisites {
			rowIndex := indexOf(objects, dep)
			adjacencyMatrix[rowIndex][colIndex] = 1
		}
	}
	return adjacencyMatrix
}


// TODO: interface for this?
func printMatrix(matrix Matrix) {
	for _, row := range matrix {
		fmt.Println(row)
	}
}


// TODO: library function or other way?
func count(arr []int, value int) int {
	total := 0
	for _, v := range arr {
		if v == value {
			total += 1
		}
	}
	return total
}


func getExecutable(adjacencyMatrix Matrix) int {
	// get node with no direct connects to other nodes (the final leaf node)
	for i, row := range adjacencyMatrix {
		if count(row, 0) == len(row) {
			// row is all zeroes
			return i
		}
	}
	return -1
}


func contains(arr []int, value int) bool {
	for _, v := range arr {
		if v == value {
			return true
		}
	}
	return false
}


func printPath(path []int, objectIndex []string) {
	namedPath := make([]string, 0, len(path))
	for _, object := range path {
		namedPath = append(namedPath, objectIndex[object])
	}
	fmt.Println(strings.Join(namedPath, " -> "))
}


func DFS(adjacencyMatrix Matrix, current int, destination int,
		 path_idx int, paths [][]int, visited []int, objectIndex []string) [][]int {
	// fmt.Printf("call with vertex: %d, path index: %d, paths: %v, visited: %v\n", 
	// 			current, path_idx, paths, visited)
	visited = append(visited, current)
	paths[path_idx] = append(paths[path_idx], current)

	if current != destination {
		// check neighbours
		row := adjacencyMatrix[current]
		numNeighbours := 0

		oldPaths := make([][]int, len(paths))
		copy(oldPaths, paths)

		for vertex, edge := range row {
			if edge == 1 && !contains(visited, vertex) {
				if numNeighbours > 0 {
					// skip the first neighbour
					// fmt.Printf("copying: %v\n", oldPaths[len(oldPaths)-1])
					paths = append(paths, oldPaths[len(oldPaths)-1])
					// fmt.Printf("new paths: %v\n", paths)
				}
				path_index := path_idx + numNeighbours
				DFS(adjacencyMatrix, vertex, destination, path_index, paths, visited, objectIndex)
				numNeighbours += 1
			}
		}
	}
	// fmt.Printf("base case with vertex: %d, paths: %v\n", current, paths)
	return paths
}


func BFS(adjacencyMatrix Matrix, current int, destination int, visited []int) []int {
	if !contains(visited, current) {
		visited = append(visited, current)
	}

	if current != destination {
		// TODO: move this to a "getNeighbours" function
		row := adjacencyMatrix[current]
		
		// iterate to visit
		for vertex, edge := range row {
			if edge == 1 && !contains(visited, vertex) {
				visited = append(visited, vertex)
			}
		}

		// iterate to perform BFS
		for vertex, edge := range row {
			if edge == 1 {
				visited = BFS(adjacencyMatrix, vertex, destination, visited)
			}
		}
	}
	return visited
}


func main() {
	var args = os.Args[1:]
	// fmt.Printf("%v\n", args)
	if len(args) == 1 && args[0] == "-h" {
		// help
		fmt.Printf(help)
	} else if len(args) == 1 {
		// makefile
		var filename = args[0]
		// initial representation for makefile
		depMap := readDependencyMap(filename)
		// adjacency matrix for graph representation	
		adjacencyMatrix := buildGraph(depMap)

		// 1. print the adjacency matrix
		printMatrix(adjacencyMatrix)
		fmt.Println()

		// 2. all make paths
		objectIndex := getObjectIndex(depMap)
		executable := getExecutable(adjacencyMatrix)
		if executable == -1 {
			error("Executable could not be determined.")
		}

		for objectId, _ := range objectIndex {
			// we want to skip starting from the executable
			if objectId != executable {
				// fmt.Printf("%d: %v\n", objectId, objectName)
				paths := make([][]int, 1)
				visited := make([]int, 0)
				paths = DFS(adjacencyMatrix, objectId, executable, 0, paths, visited, objectIndex)
				// fmt.Printf("final paths: %v\n", paths)
				for _, path := range paths {
					printPath(path, objectIndex)
				}
			}
		}
	} else if len(args) == 2 {
		// makefile dependency

		// TODO: refactor this repeated code into a function
		var filename = args[0]
		var modified = args[1]  // recently modified file

		depMap := readDependencyMap(filename)
		adjacencyMatrix := buildGraph(depMap)

		executable := getExecutable(adjacencyMatrix)
		if executable == -1 {
			// TODO: move this to getExecutable
			error("Executable could not be determined.")
		}

		objectIndex := getObjectIndex(depMap)
		modifiedIndex := indexOf(objectIndex, modified)
		if modifiedIndex == -1 {
			// unknown file
			error("Modified file not found in dependency graph")
		} else if modifiedIndex == executable {
			// nothing to do
			fmt.Println()
		} else {
			// check how to get to file with BFS
			visited := make([]int, 0)
			path := BFS(adjacencyMatrix, modifiedIndex, executable, visited)

			for _, objectId := range path {
				object := objectIndex[objectId]
				if target, ok := depMap[object] ; ok {
					// object is a target, print its recipe
					fmt.Println(target.recipe)
				}
			}
		}

	} else {
		// something else
		error("Arguments not understood")
	}
}
