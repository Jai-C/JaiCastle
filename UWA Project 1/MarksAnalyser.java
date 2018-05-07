import java.util.ArrayList;

/**
 * MarksAnalyser stores a collection of Student records.
 * Complete the code missing from methods below for practice
 * at using ArrayList and for-each loops
 * 
 * @author Jai Castle (from Michael Kölling and David J. Barnes)
 * @version 26/3/2018
 */
public class MarksAnalyser
{
    /*
     * Arbitrary length list of Student objects representing a 
     * specific group of students for a unit or lab class.
     */
    private ArrayList<Student> courselist;

    /**
     * Constructor for objects of class MarksAnalyser
     */
    public MarksAnalyser()
    {
        courselist = new ArrayList<>();
    }

    /**
     * Add a new student record to the class list.
     * @param member The Student object to be added.
     */
    public void joinClass(Student student)
    {
        courselist.add(student);
    }

    /**
     * @return The number of students (Student objects) in the class list.
     */
    public int numberOfStudents()
    {
        return courselist.size();
    }

    /**
     * Generate a class list of comma separated student names and marks 
     * in a string with a newline after each student
     * @return String list of names and marks separated by commas and newlines
     */
    public String showCourse() 
    {
        String classList = "";
        for (Student currentStudent: courselist){
            classList += currentStudent.getName();
            classList += ", ";
            classList += currentStudent.getMark();
            classList += "\n";
        }
        return classList;
    }

    /**
     * Generate a class list of student names (only) in a string
     * @return String list of names separated by newlines
     */
    public String showCourseNames() 
    {   
        String classList = "";
        for (Student currentStudent: courselist){
            classList += currentStudent.getName();
            classList += "\n";
        }
        return classList;
    }

    /**
     * Get a specific Student object record from the class list
     * @param String name of the student in the class list
     * @return Student object if the name is present or 
     * null if the name does not appear in the class list
     */
    public Student findStudent(String name) 
    {
        for (Student currentStudent: courselist){
            if (currentStudent.getName() == name){
                return currentStudent;
            }
        }
        return null;
    }

    /**
     * Find the minimum mark value, ignoring the student name
     * @return int the smallest of all values in the class list
     */
    public int minimum()
    {
        if (courselist.size() == 0) {
            return 0; // if no-one is in the class
        }
        int minimum = courselist.get(0).getMark();
        for (Student currentStudent: courselist){
            int currentMark = currentStudent.getMark();
            if (currentMark < minimum){
                minimum = currentMark;
            }
        }
        return minimum;
    }

    /**
     * Find the maximum mark in the ArrayList
     * @return int the largest value in the marks ArrayList
     */
    public int maximum()
    {
        if (courselist.size() == 0) {
            return 0; // if no-one is in the class
        }
        int maximum = courselist.get(0).getMark();
        for (Student currentStudent: courselist){
            int currentMark = currentStudent.getMark();
            if (currentMark > maximum){
                maximum = currentMark;
            }
        }
        return maximum;
    }

    /**
     * Find the average mark for the class list
     * @return double average value
     */
    public double average()
    {
        double sum = 0;
        for (Student currentStudent: courselist){
            sum += currentStudent.getMark();
        }
        double average = (sum/(courselist.size()));
        return average;
    }

    /**
     * Find the population standard deviation of marks in the class list
     * (see http://en.wikipedia.org/wiki/Standard_deviation)
     * You will need the functions Math.pow and Math.sqrt from the Math library
     * @return double value of the population standard deviation
     */
    public double standardDeviation()
    {
        double squareDifferenceSum = 0;
        double average = average();
        for (Student currentStudent: courselist){
            squareDifferenceSum += Math.pow((currentStudent.getMark() - average),2);
        }
        double n = courselist.size();
        double sDev = Math.pow(squareDifferenceSum/(n - 1),0.5);
        return sDev;
    }

    /**
     * Find all students with a mark of threshold or above.
     * @param int threshold only Students with a mark of 
     *        at least threshold are returned
     * @return ArrayList of all Students who meet the cut off
     */
    public ArrayList<Student> starStudents(int threshold)
    {
        ArrayList<Student> listOfStudents = new ArrayList<Student>();
        for (Student currentStudent: courselist){
            if (currentStudent.getMark() >= threshold){
                listOfStudents.add(currentStudent);
            }
        }
        return listOfStudents;  
    }

}
