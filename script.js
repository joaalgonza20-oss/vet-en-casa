/* JVet en Casa: estado de atención y asistente de agendamiento */
(function () {
  var PHONE = "56964632264";

  /* ---- ¿Atendiendo ahora? (hora de Chile) ---- */
  function chileNow() {
    var parts = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/Santiago", weekday: "short", hour: "numeric", minute: "numeric", hour12: false
    }).formatToParts(new Date());
    var o = {};
    parts.forEach(function (p) { o[p.type] = p.value; });
    var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return { day: days[o.weekday], mins: (parseInt(o.hour, 10) % 24) * 60 + parseInt(o.minute, 10) };
  }
  var HOURS = { 1: [540, 1140], 2: [540, 1140], 3: [540, 1140], 4: [540, 1140], 5: [540, 1140], 6: [600, 840] };
  var NAMES = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  function fmt(m) { return String(Math.floor(m / 60)).padStart(2, "0") + ":" + String(m % 60).padStart(2, "0"); }
  function status() {
    var n = chileNow(), h = HOURS[n.day];
    if (h && n.mins >= h[0] && n.mins < h[1]) return { open: true, text: "Atendiendo ahora, hasta las " + fmt(h[1]) };
    if (h && n.mins < h[0]) return { open: false, text: "Hoy desde las " + fmt(h[0]) + ". Puedes escribir y te responde al abrir" };
    for (var i = 1; i <= 7; i++) {
      var d = (n.day + i) % 7;
      if (HOURS[d]) return { open: false, text: "Fuera de horario. Vuelve " + (i === 1 ? "mañana" : "el " + NAMES[d]) + " a las " + fmt(HOURS[d][0]) };
    }
  }
  try {
    var s = status();
    document.querySelectorAll("[data-open-status]").forEach(function (el) {
      el.textContent = s.text;
      el.classList.toggle("is-open", s.open);
    });
  } catch (e) { /* sin Intl: no se muestra el estado */ }

  /* ---- Botón fijo de WhatsApp en móvil: se oculta mientras se ve el inicio o el formulario ---- */
  var cta = document.querySelector(".mobile-cta");
  var watch = [document.querySelector(".hero"), document.getElementById("contacto")].filter(Boolean);
  if (cta && watch.length && "IntersectionObserver" in window) {
    var visible = new Set();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { e.isIntersecting ? visible.add(e.target) : visible.delete(e.target); });
      cta.classList.toggle("is-hidden", visible.size > 0);
    }, { threshold: 0.15 });
    watch.forEach(function (el) { io.observe(el); });
  }

  /* ---- Asistente de agendamiento ---- */
  var form = document.getElementById("book-form");
  if (!form) return;
  var bubble = document.getElementById("bubble");
  var felv = form.querySelector('option[value="Test FeLV/FIV"]');

  function val(name) {
    var el = form.elements[name];
    if (!el) return "";
    if (el.length !== undefined && !el.tagName) {
      for (var i = 0; i < el.length; i++) if (el[i].checked) return el[i].value;
      return "";
    }
    return (el.value || "").trim();
  }
  function line(label, value, placeholder) {
    return "- " + label + ": " + (value ? esc(value) : '<span class="ph">' + placeholder + "</span>");
  }
  function esc(t) { return t.replace(/[&<>]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]; }); }

  function message(asHtml) {
    var sp = val("especie"), nom = val("nombre"), edad = val("edad");
    var pet = [sp ? sp.toLowerCase() : "", edad].filter(Boolean).join(", ");
    var mascota = nom ? nom + (pet ? " (" + pet + ")" : "") : pet;
    var rows = [
      ["Mascota", mascota, "nombre, especie y edad"],
      ["Motivo", val("motivo"), "qué necesitas"],
      ["Comuna", val("comuna"), "dónde te visitamos"],
      ["Horario preferido", val("horario"), "cuándo te acomoda"]
    ];
    var det = val("detalle");
    if (asHtml) {
      var out = "Hola Joaquín, quiero agendar una visita veterinaria a domicilio.\n" +
        rows.map(function (r) { return line(r[0], r[1], r[2]); }).join("\n");
      if (det) out += "\n- Detalle: " + esc(det);
      return out;
    }
    var txt = "Hola Joaquín, quiero agendar una visita veterinaria a domicilio.\n" +
      rows.filter(function (r) { return r[1]; }).map(function (r) { return "- " + r[0] + ": " + r[1]; }).join("\n");
    if (det) txt += "\n- Detalle: " + det;
    return txt;
  }

  function update() {
    if (felv) {
      var isDog = val("especie") === "Perro";
      felv.disabled = isDog;
      if (isDog && form.elements.motivo.value === "Test FeLV/FIV") form.elements.motivo.value = "";
    }
    bubble.innerHTML = message(true);
  }
  form.addEventListener("input", update);
  form.addEventListener("change", update);
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    window.open("https://wa.me/" + PHONE + "?text=" + encodeURIComponent(message(false)), "_blank", "noopener");
  });
  update();
})();
