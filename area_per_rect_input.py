#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Sept. 26th, 2023
# This program asks the user for the length and
# width of the rectangle in cm.
# It then calculates and displays the area and perimeter.
import math


def main():
    # Getting the length and width from the user
    print("Today we will calculate the area and")
    print("perimeter of a rectangle!")
    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))

    # Calculating the area and perimeter of the rectangle
    area = length * width
    perimeter = 2 * (length + width)

    # Displaying the area and perimeter of the rectangle
    print("")
    print("Area = {} cm^2".format(area))
    print("Perimeter = {} cm".format(perimeter))


if __name__ == "__main__":
    main()
