import re

class PolinomioModel:
    def __init__(self):
        self.terminos = []  # lista de tuplas (coeficiente, exponente)

    def parsear(self, texto):
        """
        Convierte un string en una lista de términos.
        Retorna True si fue válido, False si no.
        """
        texto = texto.replace(" ", "")
        if texto == "":
            return False

        # separa en términos manteniendo el signo
        patron = re.findall(r'[+-]?[^+-]+', texto)
        if not patron:
            return False

        self.terminos = []
        for termino in patron:
            coef, exp = self._analizar_termino(termino)
            if coef is None:
                return False
            self.terminos.append((coef, exp))
        return True

    def _analizar_termino(self, termino):
        """Analiza un termino individual y devuelve (coeficiente, exponente)."""
        termino = termino.strip()

        # caso: solo un numero, ej "-5"
        if 'x' not in termino:
            try:
                return float(termino), 0
            except ValueError:
                return None, None

        # separar coeficiente y exponente alrededor de la x
        partes = termino.split('x')
        coef_str = partes[0]
        resto = partes[1] if len(partes) > 1 else ""

        # coeficiente
        if coef_str in ("", "+"):
            coef = 1.0
        elif coef_str == "-":
            coef = -1.0
        else:
            try:
                coef = float(coef_str)
            except ValueError:
                return None, None

        # exponente
        if resto.startswith("^"):
            try:
                exp = int(resto[1:])
            except ValueError:
                return None, None
        else:
            exp = 1

        return coef, exp

    def obtener_polinomio_formateado(self):
        """Devuelve el polinomio ya ordenado y formateado como string."""
        if not self.terminos:
            return ""

        # ordenar de mayor a menor exponente
        ordenados = sorted(self.terminos, key=lambda t: t[1], reverse=True)

        partes_texto = []
        for i, (coef, exp) in enumerate(ordenados):
            partes_texto.append(self._formatear_termino(coef, exp, es_primero=(i == 0)))

        return " ".join(partes_texto)

    def _formatear_termino(self, coef, exp, es_primero):
        signo = ""
        if coef >= 0:
            signo = "" if es_primero else "+ "
        else:
            signo = "- "
            coef = abs(coef)

        # formatear coeficiente sin decimales innecesarios
        coef_str = str(int(coef)) if coef == int(coef) else str(coef)

        if exp == 0:
            return f"{signo}{coef_str}"
        elif exp == 1:
            if coef == 1:
                return f"{signo}x"
            return f"{signo}{coef_str}x"
        else:
            if coef == 1:
                return f"{signo}x^{exp}"
            return f"{signo}{coef_str}x^{exp}"