from html import escape
from pathlib import Path
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://jvetencasa.cl"
PHONE = "56964632264"

COMUNAS = [
    {
        "name": "Concepción", "slug": "concepcion",
        "intro": "Agenda una consulta veterinaria a domicilio para tu perro o gato en Concepción. Recibe atención profesional directamente en tu hogar, evitando traslados y salas de espera.",
        "description": "Consulta veterinaria, vacunas, microchip y chequeos a domicilio en Concepción. Atención para perros y gatos con agenda por WhatsApp."
    },
    {
        "name": "San Pedro de la Paz", "slug": "san-pedro-de-la-paz",
        "intro": "Coordina atención veterinaria a domicilio para perros y gatos en San Pedro de la Paz, con una visita profesional y personalizada directamente en tu hogar.",
        "description": "Veterinario a domicilio en San Pedro de la Paz para consultas, vacunas, microchip y chequeos. Agenda para perros y gatos por WhatsApp."
    },
    {
        "name": "Chiguayante", "slug": "chiguayante",
        "intro": "Agenda una consulta veterinaria a domicilio para tu perro o gato en Chiguayante. Recibe atención profesional directamente en tu hogar, evitando traslados y salas de espera.",
        "description": "Consulta veterinaria, vacunación, microchip y prevención a domicilio en Chiguayante. Atención cercana para perros y gatos."
    },
    {
        "name": "Talcahuano", "slug": "talcahuano",
        "intro": "Recibe atención veterinaria para tu perro o gato directamente en tu hogar en Talcahuano, con coordinación previa y orientación clara para cada paciente.",
        "description": "Veterinario a domicilio en Talcahuano: consultas, vacunas, microchip y chequeos para perros y gatos. Reserva por WhatsApp."
    },
    {
        "name": "Penco", "slug": "penco",
        "intro": "Coordina una visita veterinaria a domicilio en Penco para atender a tu perro o gato en un entorno conocido, cómodo y con menos estrés.",
        "description": "Atención veterinaria a domicilio en Penco para perros y gatos. Consulta, vacunas, microchip y chequeos con agenda por WhatsApp."
    },
    {
        "name": "Hualpén", "slug": "hualpen",
        "intro": "Agenda atención veterinaria a domicilio para perros y gatos en Hualpén, con evaluación profesional, indicaciones claras y seguimiento por WhatsApp.",
        "description": "Veterinario en Hualpén a domicilio para consultas, vacunas, microchip y atención preventiva de perros y gatos. Agenda por WhatsApp."
    },
]

SERVICES = [
    ("Consulta por enfermedad", "Evaluación clínica en casa para perros y gatos con signos de enfermedad, decaimiento o cambios en su estado general.", "/gatito-servicio.png", "Gato durante una consulta veterinaria a domicilio", "/#servicios"),
    ("Vacunación para perros y gatos", "Evaluación veterinaria previa, certificado y orientación personalizada según especie, raza, edad y necesidades del paciente.", "/cachorro-servicio.png", "Cachorro durante una vacunación veterinaria a domicilio", "/#vacunas"),
    ("Microchip e inscripción", "Aplicación de microchip con los formularios impresos necesarios e inscripción junto al tutor durante la consulta.", "/gato-servicio.png", "Mascota atendida por JVet en Casa para microchip", "/#servicios"),
    ("Chequeo preventivo con exámenes", "Evaluación general con hemograma y perfil bioquímico incluidos, más explicación posterior de los resultados.", "/perro-geriatrico-servicio.png", "Perro en chequeo preventivo veterinario a domicilio", "/#servicios"),
]

def analytics():
    return """<script async src="https://www.googletagmanager.com/gtag/js?id=G-MX7EMP1ES6"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-MX7EMP1ES6');</script>"""

def head(title, description, canonical, image_alt, schema):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  {analytics()}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="author" content="Méd. Vet. Joaquín González">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="geo.region" content="CL-BI">
  <link rel="canonical" href="{canonical}">
  <meta property="og:locale" content="es_CL">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="JVet en Casa">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/foto-portada.jpg">
  <meta property="og:image:alt" content="{escape(image_alt)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="{BASE}/foto-portada.jpg">
  <link rel="icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#04342C">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/cobertura/cobertura.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>
</head>"""

def header():
    return """<header class="topbar">
  <div class="container nav">
    <a href="/#inicio" class="brand"><img class="brand-logo" src="/logo-jvet-en-casa.png" alt="Logo JVet en Casa"><div class="brand-copy"><strong>JVet en Casa</strong><span>Méd. Vet. Joaquín González</span></div></a>
    <nav class="menu" aria-label="Navegación principal">
      <a href="/#inicio">Inicio</a><a href="/#servicios">Servicios</a><a href="/#vacunas">Vacunas</a><a href="/cobertura/" aria-current="page">Cobertura</a><a href="/#como-funciona">Cómo funciona</a><a href="/#contacto">Contacto</a>
      <a class="btn btn-primary" href="https://wa.me/56964632264?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20veterinaria%20a%20domicilio." target="_blank" rel="noopener noreferrer">Agenda tu visita</a>
    </nav>
  </div>
</header>"""

def footer(whatsapp):
    return """<a class="whatsapp-float" href="__WHATSAPP__" target="_blank" rel="noopener noreferrer" aria-label="Escribir a JVet en Casa por WhatsApp" title="Escríbenos por WhatsApp">✆</a>
<footer><div class="container"><p>© <span id="year"></span> JVet en Casa · Méd. Vet. Joaquín González</p></div></footer>
<script>document.getElementById('year').textContent=new Date().getFullYear();document.querySelectorAll('a[href^="https://wa.me/"]').forEach(function(a){a.addEventListener('click',function(){if(typeof gtag==='function'){gtag('event','whatsapp_click',{event_category:'contacto',event_label:a.textContent.trim()||'WhatsApp',transport_type:'beacon'})}})});</script>
</body></html>""".replace("__WHATSAPP__", whatsapp)

def commune_schema(c):
    url = f"{BASE}/cobertura/{c['slug']}/"
    faqs = [
        (f"¿Qué servicios veterinarios están disponibles en {c['name']}?", "JVet en Casa coordina consultas por enfermedad, vacunación, microchip e inscripción y chequeos preventivos con exámenes, según disponibilidad y evaluación del paciente."),
        (f"¿Cómo agendo una visita veterinaria en {c['name']}?", f"Escribe por WhatsApp indicando que necesitas atención en {c['name']}, el motivo de consulta y los datos básicos de tu perro o gato."),
        ("¿La vacunación incluye evaluación veterinaria?", "Sí. Antes de vacunar se realiza una evaluación veterinaria y se entrega certificado, junto con orientación personalizada."),
    ]
    return [
        {"@context":"https://schema.org","@type":["VeterinaryCare","LocalBusiness"],"@id":f"{BASE}/#negocio","name":"JVet en Casa","url":url,"image":f"{BASE}/foto-portada.jpg","telephone":"+56964632264","email":"jvetencasa@gmail.com","priceRange":"$$","areaServed":{"@type":"City","name":c["name"]},"founder":{"@type":"Person","name":"Joaquín González","jobTitle":"Médico veterinario"},"hasOfferCatalog":{"@type":"OfferCatalog","name":f"Servicios veterinarios a domicilio en {c['name']}","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s[0],"areaServed":{"@type":"City","name":c["name"]}}} for s in SERVICES]}},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":f"{BASE}/"},{"@type":"ListItem","position":2,"name":"Cobertura","item":f"{BASE}/cobertura/"},{"@type":"ListItem","position":3,"name":c["name"],"item":url}]},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]},
    ]

def commune_page(c):
    name, slug = c["name"], c["slug"]
    canonical = f"{BASE}/cobertura/{slug}/"
    title = f"Veterinario a domicilio en {name} | JVet en Casa"
    message = quote(f"Hola, quiero consultar disponibilidad para una atención veterinaria a domicilio en {name}.")
    wa = f"https://wa.me/{PHONE}?text={message}"
    cards = "".join(f"""<article class="service-card"><img src="{img}" alt="{escape(alt)}" loading="lazy" width="700" height="450"><div class="service-copy"><h3>{escape(service)} en {escape(name)}</h3><p>{escape(text)}</p><a class="text-link" href="{link}">Conocer más →</a></div></article>""" for service,text,img,alt,link in SERVICES)
    faqs = f"""<details class="faq-item"><summary>¿Cómo agendo una consulta veterinaria a domicilio en {escape(name)}?</summary><p>Escríbenos por WhatsApp indicando tu comuna, el motivo de consulta y los datos básicos de tu perro o gato. Confirmaremos disponibilidad antes de la visita.</p></details>
    <details class="faq-item"><summary>¿Qué vacunas se realizan a domicilio?</summary><p>Se coordinan vacunas para cachorros, gatitos y mascotas adultas, con evaluación veterinaria previa, certificado y orientación personalizada.</p></details>
    <details class="faq-item"><summary>¿El microchip incluye la inscripción?</summary><p>Sí. Se llevan los documentos impresos y la inscripción se realiza junto al tutor durante la consulta.</p></details>
    <details class="faq-item"><summary>¿JVet en Casa tiene una clínica física en {escape(name)}?</summary><p>No. JVet en Casa es un servicio veterinario a domicilio: el médico veterinario se traslada directamente hasta tu hogar.</p></details>"""
    return f"""{head(title,c['description'],canonical,f'Atención veterinaria a domicilio de JVet en Casa en {name}',commune_schema(c))}
<body>{header()}
<main>
  <nav class="breadcrumb container" aria-label="Migas de pan"><ol><li><a href="/">Inicio</a></li><li>›</li><li><a href="/cobertura/">Región del Biobío</a></li><li>›</li><li aria-current="page">{escape(name)}</li></ol></nav>
  <section class="hero"><div class="container hero-grid"><div><span class="badge">Veterinaria a domicilio para perros y gatos</span><h1>Veterinario a domicilio en {escape(name)}</h1><p class="lead">{escape(c['intro'])}</p><p class="trust-line">Atención directa con el Méd. Vet. Joaquín González.</p><div class="price-note">Promoción vigente: consulta a domicilio $20.000 durante julio</div><div class="hero-actions"><a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener noreferrer">Agendar visita</a><a class="btn btn-secondary" href="/#servicios">Ver servicios y precios</a></div></div><div class="hero-photo"><img src="/foto-portada.jpg" alt="Méd. Vet. Joaquín González durante una atención veterinaria a domicilio en {escape(name)}" width="900" height="900"></div></div></section>
  <section><div class="container"><div class="section-title"><h2>Servicios veterinarios disponibles en {escape(name)}</h2><p>Atención clínica y preventiva para perros y gatos, conservando los precios y promociones publicados por JVet en Casa.</p></div><div class="service-grid">{cards}</div></div></section>
  <section><div class="container"><div class="section-title"><h2>Beneficios de la atención veterinaria a domicilio</h2><p>Una experiencia más cómoda para tu mascota y para ti.</p></div><div class="benefit-grid"><article class="benefit-card"><h3>Menos estrés</h3><p>Evita traslados, salas de espera y cambios bruscos de ambiente.</p></article><article class="benefit-card"><h3>Atención personalizada</h3><p>Evaluación directa con el Méd. Vet. Joaquín González e indicaciones claras.</p></article><article class="benefit-card"><h3>Seguimiento por WhatsApp</h3><p>Coordinación sencilla y acompañamiento posterior cuando corresponde.</p></article></div></div></section>
  <section><div class="container clinic-copy"><h2>¿Buscas una clínica veterinaria en {escape(name)}?</h2><p>JVet en Casa ofrece una alternativa cómoda para consultas generales, vacunación y atención preventiva: un médico veterinario se traslada directamente hasta tu hogar.</p></div></section>
  <section><div class="container"><div class="section-title"><h2>Preguntas frecuentes sobre atención en {escape(name)}</h2></div><div class="faq-list">{faqs}</div></div></section>
  <section><div class="container final-cta"><h2>Agenda atención veterinaria en {escape(name)}</h2><p>Cuéntanos qué necesita tu mascota y consulta disponibilidad para una visita a domicilio.</p><a class="btn btn-secondary" href="{wa}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a></div></section>
</main>{footer(wa)}"""

def coverage_page():
    canonical = f"{BASE}/cobertura/"
    title = "Cobertura veterinaria a domicilio | JVet en Casa"
    description = "Conoce la cobertura de JVet en Casa para consultas, vacunas, microchip y chequeos veterinarios a domicilio en el Gran Concepción."
    schema = [{"@context":"https://schema.org","@type":["VeterinaryCare","LocalBusiness"],"@id":f"{BASE}/#negocio","name":"JVet en Casa","url":canonical,"telephone":"+56964632264","areaServed":[{"@type":"City","name":c["name"]} for c in COMUNAS]},{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":f"{BASE}/"},{"@type":"ListItem","position":2,"name":"Cobertura","item":canonical}]}]
    cards = "".join(f"""<a class="coverage-card" href="/cobertura/{c['slug']}/"><h2>{escape(c['name'])}</h2><p>Veterinario a domicilio para perros y gatos en {escape(c['name'])}.</p></a>""" for c in COMUNAS)
    wa = "https://wa.me/56964632264?text=Hola%2C%20quiero%20consultar%20si%20tienen%20cobertura%20en%20mi%20comuna."
    return f"""{head(title,description,canonical,'Cobertura de atención veterinaria a domicilio de JVet en Casa',schema)}
<body>{header()}<main><nav class="breadcrumb container" aria-label="Migas de pan"><ol><li><a href="/">Inicio</a></li><li>›</li><li aria-current="page">Cobertura</li></ol></nav><section class="hero"><div class="container hero-grid"><div><span class="badge">Región del Biobío</span><h1>¿Dónde atiende JVet en Casa?</h1><p class="lead">Conoce nuestra cobertura de atención veterinaria a domicilio para perros y gatos en el Gran Concepción.</p><div class="hero-actions"><a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener noreferrer">Consultar cobertura</a><a class="btn btn-secondary" href="/#servicios">Ver servicios</a></div></div><div class="hero-photo"><img src="/foto-atencion.jpg" alt="Atención veterinaria a domicilio realizada por JVet en Casa" width="900" height="900"></div></div></section><section><div class="container"><p class="region-label">Región del Biobío</p><div class="coverage-grid">{cards}</div></div></section><section><div class="container final-cta"><h2>¿Tu comuna no aparece?</h2><p>Escríbenos para consultar disponibilidad en otros sectores cercanos del Gran Concepción.</p><a class="btn btn-secondary" href="{wa}" target="_blank" rel="noopener noreferrer">Consultar por WhatsApp</a></div></section></main>{footer(wa)}"""

def main():
    coverage_dir = ROOT / "cobertura"
    coverage_dir.mkdir(exist_ok=True)
    (coverage_dir / "index.html").write_text(coverage_page(), encoding="utf-8")
    for comuna in COMUNAS:
        target = coverage_dir / comuna["slug"]
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(commune_page(comuna), encoding="utf-8")

if __name__ == "__main__":
    main()
