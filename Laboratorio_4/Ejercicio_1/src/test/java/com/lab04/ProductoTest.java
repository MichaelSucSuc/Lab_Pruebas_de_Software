package pe.com.lab04;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class ProductoTest {

    private Producto producto;

    @BeforeEach
    void setUp() {
        producto = new Producto("P001", "Laptop", 1500.0, 10);
    }

    // -------------------------------------------------------------
    // Pruebas del constructor y validaciones
    // -------------------------------------------------------------
    @Nested
    @DisplayName("Pruebas de construcción y validaciones")
    class ConstructorTests {

        @Test
        @DisplayName("Constructor válido crea producto correctamente")
        void testConstructorValido() {
            assertAll("Propiedades iniciales",
                () -> assertEquals("P001", producto.getCodigo()),
                () -> assertEquals("Laptop", producto.getNombre()),
                () -> assertEquals(1500.0, producto.getPrecio()),
                () -> assertEquals(10, producto.consultarStock())
            );
        }

        @Test
        @DisplayName("Lanza excepción si el código es null")
        void testCodigoNull() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> new Producto(null, "Mouse", 20.0, 5));
            assertEquals("El código no puede estar vacío", ex.getMessage());
        }

        @Test
        @DisplayName("Lanza excepción si el código está vacío")
        void testCodigoVacio() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> new Producto("", "Mouse", 20.0, 5));
            assertEquals("El código no puede estar vacío", ex.getMessage());
        }

        @Test
        @DisplayName("Lanza excepción si el precio no es positivo")
        void testPrecioNoPositivo() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> new Producto("P002", "Mouse", -10.0, 5));
            assertEquals("El precio debe ser positivo", ex.getMessage());
        }

        @Test
        @DisplayName("Lanza excepción si la cantidad inicial es negativa")
        void testCantidadInicialNegativa() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> new Producto("P003", "Teclado", 50.0, -1));
            assertEquals("La cantidad inicial no puede ser negativa", ex.getMessage());
        }
    }

    // -------------------------------------------------------------
    // Pruebas de gestión de stock
    // -------------------------------------------------------------
    @Nested
    @DisplayName("Pruebas de gestión de stock")
    class StockTests {

        @Test
        @DisplayName("Agregar stock incrementa correctamente")
        void testAgregarStock() {
            producto.agregarStock(5);
            assertEquals(15, producto.consultarStock());
        }

        @Test
        @DisplayName("Agregar cantidad negativa lanza excepción")
        void testAgregarStockNegativo() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> producto.agregarStock(-3));
            assertEquals("La cantidad a agregar debe ser positiva", ex.getMessage());
        }

        @Test
        @DisplayName("Extraer stock disminuye correctamente")
        void testExtraerStock() {
            producto.extraerStock(3);
            assertEquals(7, producto.consultarStock());
        }

        @Test
        @DisplayName("Extraer más stock del disponible lanza excepción")
        void testExtraerStockInsuficiente() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> producto.extraerStock(20));
            assertEquals("Stock insuficiente", ex.getMessage());
        }

        @Test
        @DisplayName("Extraer cantidad negativa lanza excepción")
        void testExtraerStockNegativo() {
            Exception ex = assertThrows(IllegalArgumentException.class,
                () -> producto.extraerStock(-2));
            assertEquals("La cantidad a extraer debe ser positiva", ex.getMessage());
        }
    }

    // -------------------------------------------------------------
    // Pruebas de valor total (incluye parametrizada)
    // -------------------------------------------------------------
    @Nested
    @DisplayName("Pruebas de cálculo de valor total")
    class ValorTotalTests {

        @Test
        @DisplayName("Valor total después de agregar stock")
        void testValorTotalConAgregar() {
            producto.agregarStock(5);
            assertEquals(1500.0 * 15, producto.obtenerValorTotal());
        }

        @Test
        @DisplayName("Valor total después de extraer stock")
        void testValorTotalConExtraer() {
            producto.extraerStock(3);
            assertEquals(1500.0 * 7, producto.obtenerValorTotal());
        }

        @ParameterizedTest
        @DisplayName("Prueba parametrizada de valor total (diferentes stocks finales)")
        @CsvSource({
            "0, 0",
            "5, 7500",
            "10, 15000",
            "20, 30000"
        })
        void testValorTotalParametrizado(int stockFinal, double expectedTotal) {
            // Ajustar desde stock inicial 10 hasta stockFinal
            if (stockFinal < 10) {
                producto.extraerStock(10 - stockFinal);
            } else if (stockFinal > 10) {
                producto.agregarStock(stockFinal - 10);
            }
            assertEquals(expectedTotal, producto.obtenerValorTotal());
        }
    }

    // -------------------------------------------------------------
    // Pruebas de historial de movimientos (incluye validación de fecha)
    // -------------------------------------------------------------
    @Nested
    @DisplayName("Pruebas de historial de movimientos")
    class HistorialTests {

        private LocalDateTime beforeTest;

        @BeforeEach
        void recordStartTime() {
            beforeTest = LocalDateTime.now();
        }

        @Test
        @DisplayName("Se crea movimiento inicial con fecha válida")
        void testMovimientoInicial() {
            assertEquals(1, producto.getMovimientos().size());
            Movimiento mov = producto.getMovimientos().get(0);
            assertEquals("ENTRADA", mov.getTipo());
            assertEquals(10, mov.getCantidad());

            assertNotNull(mov.getFecha());
            assertTrue(mov.getFecha().isAfter(beforeTest.minusSeconds(1)));
            assertTrue(mov.getFecha().isBefore(LocalDateTime.now().plusSeconds(1)));
        }

        @Test
        @DisplayName("Se registra movimiento al agregar stock con fecha válida")
        void testMovimientoAlAgregar() {
            producto.agregarStock(7);
            assertEquals(2, producto.getMovimientos().size());
            Movimiento mov = producto.getMovimientos().get(1);
            assertEquals("ENTRADA", mov.getTipo());
            assertEquals(7, mov.getCantidad());

            assertNotNull(mov.getFecha());
            assertTrue(mov.getFecha().isAfter(beforeTest.minusSeconds(1)));
            assertTrue(mov.getFecha().isBefore(LocalDateTime.now().plusSeconds(1)));
        }

        @Test
        @DisplayName("Se registra movimiento al extraer stock con fecha válida")
        void testMovimientoAlExtraer() {
            producto.extraerStock(4);
            assertEquals(2, producto.getMovimientos().size());
            Movimiento mov = producto.getMovimientos().get(1);
            assertEquals("SALIDA", mov.getTipo());
            assertEquals(4, mov.getCantidad());

            assertNotNull(mov.getFecha());
            assertTrue(mov.getFecha().isAfter(beforeTest.minusSeconds(1)));
            assertTrue(mov.getFecha().isBefore(LocalDateTime.now().plusSeconds(1)));
        }
    }
}