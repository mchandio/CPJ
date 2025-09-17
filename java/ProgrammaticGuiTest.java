import java.util.concurrent.atomic.AtomicReference;

public class ProgrammaticGuiTest {
    public static void main(String[] args) throws Exception {
        final AtomicReference<GeneratedCalculator> ref = new AtomicReference<>();

        // Create the GUI on the EDT and store reference
        javax.swing.SwingUtilities.invokeAndWait(() -> {
            GeneratedCalculator g = new GeneratedCalculator();
            g.setVisible(true);
            ref.set(g);
        });

        // Now we're on the main thread; press buttons. pressButton uses invokeAndWait
        // internally
        GeneratedCalculator g = ref.get();
        if (g == null)
            throw new IllegalStateException("GUI not created");

        // simulate: 10 + 2 =
        g.pressButton("1");
        g.pressButton("0");
        g.pressButton("+");
        g.pressButton("2");
        g.pressButton("=");

        // Read display via EDT-safe getter
        java.util.concurrent.atomic.AtomicReference<String> dispRef = new java.util.concurrent.atomic.AtomicReference<>();
        javax.swing.SwingUtilities.invokeAndWait(() -> {
            dispRef.set(g.getDisplayText());
        });
        System.out.println("DISPLAY:" + dispRef.get());
    }
}
