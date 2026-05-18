package pe.com.lab04;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Producto {
    private String codigo;
    private String nombre;
    private double precio;
    private int cantidad;
    private List<Movimiento> movimientos;

    // Constructor con validaciones
    public Producto(String codigo, String nombre, double precio, int cantidad) {
        if (codigo == null || codigo.trim().isEmpty()) {
            throw new IllegalArgumentException("El código no puede estar vacío");
        }
        if (precio <= 0) {
            throw new IllegalArgumentException("El precio debe ser positivo");
        }
        if (cantidad < 0) {
            throw new IllegalArgumentException("La cantidad inicial no puede ser negativa");
        }
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
        this.movimientos = new ArrayList<>();
        if (cantidad > 0) {
            movimientos.add(new Movimiento("ENTRADA", cantidad, LocalDateTime.now()));
        }
    }

    public void agregarStock(int cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad a agregar debe ser positiva");
        }
        this.cantidad += cantidad;
        movimientos.add(new Movimiento("ENTRADA", cantidad, LocalDateTime.now()));
    }

    public void extraerStock(int cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad a extraer debe ser positiva");
        }
        if (this.cantidad - cantidad < 0) {
            throw new IllegalArgumentException("Stock insuficiente");
        }
        this.cantidad -= cantidad;
        movimientos.add(new Movimiento("SALIDA", cantidad, LocalDateTime.now()));
    }

    public int consultarStock() {
        return cantidad;
    }

    public double obtenerValorTotal() {
        return precio * cantidad;
    }

    // Getters necesarios para pruebas
    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public List<Movimiento> getMovimientos() { return movimientos; }
}