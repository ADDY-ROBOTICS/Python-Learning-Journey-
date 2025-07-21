def main():
   month = "January"
   match month:
      case n if n in ('January', 'March', 'May') and (n.startswith('J') or n.startswith('M')):
         print('Valid Month')     
      case _:
         print('Other month')     

if __name__ == "__main__":
    main()

