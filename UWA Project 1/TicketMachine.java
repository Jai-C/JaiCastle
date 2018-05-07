/**
 * TicketMachine models a ticket machine that issues
 * flat-fare tickets.
 * The price of a ticket is specified via the constructor.
 * Instances will check to ensure that a user only enters
 * sensible amounts of money, and will only print a ticket
 * if enough money has been input.
 *
 * @ author Jai Castle (from David J. Barnes and Michael Koelling).
 * @version 2011.07.31
 */
public class TicketMachine
{
    // The price of a ticket from this machine.
    private int price;
    // The amount of money entered by a customer so far.
    private int balance;
    // The total amount of money collected by this machine.
    private int total;

    /**
     * Create a machine that issues tickets of the given price.
     * Note that the price must be greater than zero, and there
     * are no checks to ensure this.
     */
    public TicketMachine(int cost)
    {
        price = cost;
        balance = 0;
        total = 0;
    }

    /**
     * Return the price of a ticket.
     */
    public int getPrice()
    {
        return price;
    }

    /**
     * Return the amount of money already inserted for the
     * next ticket.
     */
    public int getBalance()
    {
        return balance;
    }
    
    public int getTotal(){
        return total;
    }

    /**
     * Receive an amount of money from a customer.
     */
    public void insertMoney(int amount)
    {  
        if (amount > 0 && amount <100000){
            balance = balance + amount;
        } else {
            System.out.println("Please enter a number between 0 and 100000 cents!");
        }
        if (balance >= price){
            System.out.println("You have enough money for the ticket!");
        }
    }
    
    public void setPrice(int cost){
        price = cost;
    }

    /**
     * Print a ticket.
     * Update the total collected and
     * reduce the balance to zero.
     */
    public void printTicket()
    {
        if (balance >= price){
            // Simulate the printing of a ticket.
            System.out.println("##################");
            System.out.println("# The BlueJ Line");
            System.out.println("# Ticket");
            System.out.println("# " + price + " cent.");
            System.out.println("##################");
            System.out.println();
    
            // Update the total collected with the balance.
            total = total + balance; 
            // Clear the balance.
            balance = balance - price;
            System.out.println(balance + " cents remaining in your balance.");
        } else {
            System.out.println("Please enter at least " + price + " cents before printing your ticket.");
            System.out.println("You need " + (price - balance) + " more cents.");
        }
    }
    
    //Additional method to give change by resetting the balance.
    public void giveChange(){
        System.out.println("Change to be given: " + balance + " cents.");
        balance = 0;
        System.out.println("Balance has been reset to " + balance + ".");
    }

}
