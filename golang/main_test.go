package main

import (
	"errors"
	"fmt"
	"regexp"
	"testing"
)

func TestHelloName(t *testing.T) {
	name := "Gladys"
	want := regexp.MustCompile(`\b`+name+`\b`)
	msg, err := Hello("Gladys")
	if !want.MatchString(msg) || err != nil {
			t.Fatalf(`Hello("Gladys") = %q, %v, want match for %#q, nil`, msg, err, want)
	}
}
func Hello(name string) (string, error) {
	// If no name was given, return an error with a message.
	if name == "" {
			return name, errors.New("empty name")
	}
	// Create a message using a random format.
	// message := fmt.Sprintf(randomFormat(), name)
	message := fmt.Sprint(name)
	return message, nil
}