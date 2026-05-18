package pe.com.lab04;

import java.time.LocalDateTime;

public class Movimiento {
    private String tipo;
    private int cantidad;
    private LocalDateTime fecha;

    public Movimiento(String tipo, int cantidad, LocalDateTime fecha) {
        this.tipo = tipo;
        this.cantidad = cantidad;
        this.fecha = fecha;
    }

    public String getTipo() { return tipo; }
    public int getCantidad() { return cantidad; }
    public LocalDateTime getFecha() { return fecha; }
}