def main():
   total_sum = 0
   num = 0
   while total_sum <= 15:
    total_sum += num
    num += 1
    if total_sum > 15:
        break
   print(total_sum)  # Print the total sum after the loop ends
if __name__ == "__main__":
    main()
    
