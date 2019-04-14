package main

import (
	"os"
	"sort"
	"testing"
)

func readDirNames(dirname string) ([]string, error) {
	f, err := os.Open(dirname)
	if err != nil {
		return nil, err
	}
	names, err := f.Readdirnames(-1)
	f.Close()
	if err != nil {
		return nil, err
	}
	sort.Strings(names)
	return names, nil
}

func Test_aha(t *testing.T) {
	dirs, _ := readDirNames("d:\\")
	t.Log(dirs)
}
