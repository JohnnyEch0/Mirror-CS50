void collatz(int x)
{
    if x == 1
        return 1;

    elif (argc % 2 == 0)
        return collatz(x/2);
    else
        return collatz(3*x + 1);
    printf("%i steps to Collatz %i",)
}


void main(argc, argv)
{
    if (argc != 2)
        return 1;


    collatz(argv[1]);
}
