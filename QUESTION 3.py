import turtle

# Recursive function to draw the tree
def draw_tree(t, branch_length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0:
        return
    else:
        # Draw the main branch
        t.forward(branch_length)
        
        # Draw the left branch
        t.left(left_angle)
        draw_tree(t, branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)
        
        # Go back to the main branch position
        t.right(left_angle + right_angle)
        
        # Draw the right branch
        draw_tree(t, branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)
        
        # Go back to the main branch position
        t.left(right_angle)
        t.backward(branch_length)

# Set up the screen and turtle
def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Set up the turtle
    t = turtle.Turtle()
    t.left(90)  # Start the turtle pointing upwards
    t.speed(0)  # Fastest drawing speed
    
    # Get parameters from the user
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    start_length = float(input("Enter the starting branch length (in pixels): "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))
    
    # Start drawing the tree
    draw_tree(t, start_length, depth, left_angle, right_angle, reduction_factor)
    
    # Hide the turtle after drawing
    t.hideturtle()
    
    # Keep the window open
    screen.mainloop()

# Run the program
if __name__ == "__main__":
    main()
