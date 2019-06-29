package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

var maxInput int64 = 0
var fiboSet = []int64{1,2}

func contains(s []int64, e int64) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func extendFiboSet(maxNumber int64) bool {
    maxInput = maxNumber
    var last = fiboSet[len(fiboSet)-1]
    var beforeLast = fiboSet[len(fiboSet)-2]
    var newFibo = last + beforeLast;
    for do := true; do; do = maxNumber > newFibo {
        newFibo = last + beforeLast
        beforeLast = last
        last = newFibo
        fiboSet = append(fiboSet, newFibo)
        fmt.Printf("%d\n", last)
    }

    return true;
}

// Complete the solve function below.
func solve(n int64) string {
    var RET_T = "IsFibo"
    var RET_F = "IsNotFibo"
    extendFiboSet(n)
    if contains(fiboSet, n) {
        return RET_T
    } else {
        return RET_F
    }
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    tTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)
    t := int32(tTemp)

    for tItr := 0; tItr < int(t); tItr++ {
        n, err := strconv.ParseInt(readLine(reader), 10, 64)
        checkError(err)

        result := solve(n)

        fmt.Fprintf(writer, "%s\n", result)
    }

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
