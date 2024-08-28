Start
    "Plan: Calculate Cubic Feet Storage By Refrigerator Model"
    Input Cubic_Inches_Per_Cubic_Foot = 1728
    Refrigerator_Model_Name = input ("Enter the refrigerator model name: ")
    Height_In_Inches = float(input("Enter the interior height in inches: "))
    Width_In_Inches = float(input("Enter the interior width in inches: "))
    Depth_In_Inches = float(input("Enter the interior depth in inches: "))
    Cubic_Inches = Height_In_Inches * Width_In_Inches * Depth_In_Inches
    Capacity_In_Cubic_Feet = Cubic_Inches / Cubic_Inches_Per_Cubic_Foot
    print(f"Refrigerator Model Name: {refrigerator_model_name}")
    print(f"Capacity: {capacity_in_cubic_feet:.2f} Cubic Feet")
End