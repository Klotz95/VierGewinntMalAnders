<h1>EPR Blatt 3: Vier gewinnt mal anders</h1>
<h2>Aufgabenbeschreibung</h2>
<h3>Spielprinzip</h3>
<p>Es war ein Spiel zu implementieren, welches ein typisches "Vier gewinnt"-Spiel repräsentiert. Der große Unterschied zu der normalen variante war jedoch der, das man nur dann gewinnt, wenn die Speilsteine eine Kombination darstellen, welche einem Zug des Springers gleichen.</p>
<p><em>Beispiel einer Siegkonstellation:</em></p>
<p>x x x<br>x<br>x</p>
<h3>User Interface</h3>
<p>Das User-Interface sollte schlicht gehalten werden. Sprich, es sollte lediglich eine Terminal-Applikation realisiert werden, welche die Steine der jeweilig zwei Spieler, deutlich differenziert voneinander repräsentiert.</p>
<h3>KI</h3>
<p>Für das Spiel sollte ebenfalls ein Single-Player-Mode realisiert werden. Hierbei ist es (laut Aufgabenbeschreibung) völlig egal, welcher ALgorithmus für das Realisieren genutzt wird. Natürlich könnte man einfach eine Zufallszahl generieren und an dieser Stelle den Stein fallen lassen. Diese Methode ist aber ziemlich uncool und findet innerhalb diese Projektes keine Anwendung.</p>
<h2>Module</h2>
<p>In folgender Tabelle sind alle Module aufgelistet, welche für das Lösen des Problems generiert wurden:</p>
<table>
  <thead>
    <tr>
      <th>Modul</th>
      <th>Beschreibung</th>
     </tr>
    </thead>
    <tbody>
      <tr>
        <td>userInterface.py</td>
        <td>Beinhaltet die Terminal-Darstellung des User-Interfaces. Es ist ebenfalls für die korrekte Initialisierung des                         Programms zustädnig</td>
      </tr>
      <tr>
        <td>GameCheck.py</td>
        <td>Beinhaltet den Überprüfungsalgorithmus für den Sieg eines Spielers</td>
      </tr>
      <tr>
        <td>KI.py</td>
        <td>Beinhaltet die KI für den Single-Player-Mode</td>
      </tr>
</table>
<h2>Nutzungshinweise</h2>
<p>Um das Spiel zu starten, importieren sie das Modul userInterface.py in den Python-Interpreter. </p>
