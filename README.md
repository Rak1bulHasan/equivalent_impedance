# equivalent_impedance

The program starts from the highest value of nodes and gradually goes down to 1. It identfies series connection if one components' end is connected to another component's start. If ending and starting are equal then it is treated as parallel connection. for example R1, R2, R3 have respective starting and ending at (1,2),(2,3),(1,3). So according to the logic R1 & R2 are in series and that whole branch is in parallel to R3. after each iteration the value is saved to Sum.
