1. `class Persona`:
   - Es la clase base que representa a una persona con atributos como nombre, edad y DNI. El DNI está encapsulado para proteger la privacidad.
   - El método `_str_` retorna una cadena con el nombre, edad y DNI de la persona.

2. `class Empleado` (subclase de `Persona`):
   - Agrega atributos de salario y cargo.
   - Proporciona un método `getSalario` para obtener el salario del empleado.
   - Sobrescribe el método `_str_` para incluir información sobre el salario y el cargo del empleado.

3. `class Gerente` (subclase de `Empleado`):
   - Especifica que el cargo es "Gerente" y agrega el atributo departamento.
   - Proporciona un método `getDepartamento` para obtener el departamento del gerente.
   - Sobrescribe el método `_str_` para incluir información sobre el departamento del gerente.

4. `class Departamento`:
   - Contiene un nombre, un gerente y una lista de empleados.
   - Permite agregar y eliminar empleados y obtener información sobre el gerente y los empleados del departamento.
   - El método `getPersonal` retorna una lista de todos los empleados y el gerente del departamento.

El código muestra cómo crear instancias de `Empleado` y `Gerente`, cómo agregarlos a un `Departamento`, y cómo usar los métodos definidos para manipular y obtener información sobre los empleados y el gerente. También muestra cómo imprimir la información de los empleados, añadirlos y eliminarlos del departamento, destacando la reutilización y la encapsulación de datos siguiendo los principios de la programación orientada a objetos (POO).

El ejemplo final muestra cómo:
- Se crean instancias de `Empleado` para diferentes roles como desarrolladores Full Stack, Front End y Back End.
- Se crea una instancia de `Gerente`.
- Se crea una instancia de `Departamento` asignándole un gerente y empleados.
- Se utilizan los métodos para agregar y eliminar empleados del departamento.
- Se imprime la información del departamento, el gerente y los empleados.