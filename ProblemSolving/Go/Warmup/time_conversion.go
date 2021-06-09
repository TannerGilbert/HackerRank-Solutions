package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
	"strconv"
)

func timeConversion(s string) string {
	if strings.HasSuffix(s, "AM") {
		if strings.HasPrefix(s, "12") {
			return "00" + s[2:len(s)-2]
		}
		return s[:len(s)-2]
	} else {
		if strings.HasPrefix(s, "12") {
			return s[:len(s)-2]
		}
		v, _ := strconv.Atoi(s[:2])
		return strconv.Itoa(v+12) + s[2:len(s)-2]
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Fprintf(writer, "%s\n", result)

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
