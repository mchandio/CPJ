package cpj.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;

public class ProgrammaticGuiTest {
    private GeneratedCalculator calculator;

    @BeforeEach
    public void setup() throws Exception {
        // Create the GUI on the EDT and store reference
        javax.swing.SwingUtilities.invokeAndWait(() -> {
            calculator = new GeneratedCalculator();
            calculator.setVisible(true);
        });
    }

    @AfterEach
    public void tearDown() {
        if (calculator != null) {
            calculator.dispose();
        }
    }

    @Test
    public void testBasicAddition() throws Exception {
        // simulate: 10 + 2 =
        calculator.pressButton("1");
        calculator.pressButton("0");
        calculator.pressButton("+");
        calculator.pressButton("2");
        calculator.pressButton("=");

        // Read display
        String displayText = calculator.getDisplayText();
        assertEquals("12.0", displayText, "10 + 2 should equal 12.0");
    }
}
