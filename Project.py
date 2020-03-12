
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from googlesearch import search
import requests
import numpy as np
import matplotlib.pyplot as plt
import ssl
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


fiables=0
noFiables=0
urlLista2 =['https://actualidadpanamericana.com/spark-vidrios-negros-completa-reten-1-000-000/?fbclid=IwAR3mHLO2DPdkQo2ELKiaqHOwA9EOI4qO1MKuFAMlH3c0MuRlNSZGsIrmY3o']

urlLista = [
'https://www.eltiempo.com/politica/partidos-politicos/partido-liberal-apoyara-a-los-11-millones-de-la-consulta-anticorrupcion-260534'
,"http://www.lalenguacaribe.co/petro-repitio-la-historia-de-titulos-falsos-que-tanto-critico-a-penalosa/"
,'https://www.abc.es/espana/catalunya/politica/abci-iglesias-y-junqueras-reunen-lledoners-201810191611_noticia.html'
,'https://cnnespanol.cnn.com/2018/11/06/este-objeto-espacial-con-forma-de-cigarrillo-podria-haber-sido-una-nave-extraterrestre-segun-astronomos-de-harvard/'
,'https://actualidadpanamericana.com/facebook-habilita-para-colombia-estatus-se-siente-bendecida-y-afortunada/'
,'https://actualidadpanamericana.com/gobierno-usara-aviones-de-uber-para-defender-frontera-con-venezuela/'
,'https://colombianoindignado.com/se-la-mando-james-con-carino-el-segundo-mandado-que-hace-duque-en-el-exterior/?fbclid=IwAR2TgpiSkboKGi0tAeendG1E0RqYVW3mO7D2Nu3GSWhuB5Y6ObZbObLvvMQ'
,'https://www.elplanetacurioso.com/2018/10/22/tener-novia-enojona-es-bueno-para-la-salud-segun-estudios-2/?fbclid=IwAR3vXzVVJ5W5CDhbvpChJ8MSjvJEPVvnjY5u0CF5A-khouyViI9g0--Usww'
,'https://www.vuntu.co/2018/11/7-cosas-que-jamas-debes-decir-tu-pareja.html?fbclid=IwAR0kKTdEf12fHXqsrLnazjCRICs_9P01_9NAOp60ZmTvLRpjrtv5o5CN1tg'
,'https://noticiasopinion.com/miss-colombia-aparece-caso-cerrado/?fbclid=IwAR08pEhywQ9I7oTp0G2Tc7hP1fVp0f0FM4sDZa9EYA8JRFa-yerdrwzg-Ic'
,'https://noticiasopinion.com/75-uber-cancelaron-licencia/?fbclid=IwAR1hiU4e0b9qE1tFPzca3UaKGOPuwVZWqzvXYUA2Q3gT9cTk_Ovz4QyConA'
,'https://noticiasnube.com/juan-valdez-recibio-el-sello-empresa-incluyente?utm_campaign=Noticias+Nube&utm_medium=facebook&utm_source=socialnetwork&fbclid=IwAR3RqTaFUEE4Mw1YuM5_VP21OU27a2Rd36Yv3LcEykAt80O9JZARR5iIyzY'
,'https://noticiasnube.com/libertadores-final-se-jugara-fuera-de-argentina-entre-8-y-9-de-diciembre?utm_campaign=Noticias+Nube&utm_medium=facebook&utm_source=socialnetwork&fbclid=IwAR0cZBNuxBmFxoFdK10gfz9iZb_EKzCcw18znyrcMb9nMxwEdjdTYpBxjoA'
,'https://noticiasnube.com/dieron-de-baja-a-cabecilla-del-eln-alias-miller-en-el-choco?utm_campaign=Noticias+Nube&utm_medium=facebook&utm_source=socialnetwork&fbclid=IwAR1nFEOdDpB7flo3Y1qltKcW5yWROEbr9RXDe1CWCXYli2IEr6kj5AMdOW4'
,'https://noticiasnube.com/abatieron-a-cuatro-implicados-en-asesinato-de-geologos-en-antioquia?utm_campaign=Noticias+Nube&utm_medium=facebook&utm_source=socialnetwork&fbclid=IwAR2ebw3A5nJE87-O740TxqUudDoDlgxKFArWSpfVJ2toAhEV3Baoo2zcwFA'
,'https://www.mundo.com/actualidad/modelo-fue-asesinada-y-su-hijo-permanecio-cinco-dias-junto-al-cadaver/'
,'https://www.mundo.com/actualidad/estados-unidos-agrego-nuevas-restricciones-para-equipaje/'
,'http://www.elhomenoticias.com/justicia/confirmado-si-son-guacho-y-pitufin-medicina-legal/?fbclid=IwAR0dU4rEOjAQbRuICjwW2qTrh8XRMZsKoJKdzmlm8c9hOQwXuTlG-c9uXkI'
,'http://www.elhomenoticias.com/politica/no-votaria-por-gustavo-petro-urrego-porque-ese-video-es-muy-sucio-simon-velez/?fbclid=IwAR1vC6bqV1RfbktmYQyVV3okZJ7HiEEYa2KrCCFluGZW17276J-E1SGEVQI'
,'http://www.elhomenoticias.com/politica/los-fajos-de-billetes-que-recibio-gustavo-petro-fueron-por-el-contrato-de-la-maquina-tapahuecos/?fbclid=IwAR1l0Q_WBn9GqHwfWFjCQtZSDBMvkWd9b7OVPHdeybWaKIRSwrRlhauJ7vU'
,'http://www.elhomenoticias.com/justicia/por-que-capturaron-a-luis-francisco-perdomo-director-de-la-picota/?fbclid=IwAR1NbCf-Ad0i2LiSSBTeG21c5XneUA9F_hjWVVyKk-GZDjamAv4LoDqFOcE'
,'https://www.noticiasaldiayalahora.co/internacionales/detuvieron-a-seis-sujetos-por-comerse-a-un-mono-y-transmitirlo-en-facebook/?fbclid=IwAR3Q9y4qI44HsR5w5GDJkW4fl2iEGVeqTkyHFKqitU0snI6nN2JTBfnIbyo'
,'https://www.noticiasaldiayalahora.co/internacionales/detuvieron-a-seis-sujetos-por-comerse-a-un-mono-y-transmitirlo-en-facebook/?fbclid=IwAR3Q9y4qI44HsR5w5GDJkW4fl2iEGVeqTkyHFKqitU0snI6nN2JTBfnIbyo'
,'https://www.colombian.com.co/judicial/video-reclusos-protagonizaron-batalla-campal-en-una-uri-de-bogota/?fbclid=IwAR0ew3pzBA_5DYJSjaknpJizb5UAiopQEmeFIk2GW64HO_NoWbseWISydSE'
,'https://www.colombian.com.co/actualidad/hombre-espiaba-con-una-camara-a-una-mujer-mientras-se-media-ropa-en-almacen-en-bogota/?fbclid=IwAR2_rwD47_ZiRVzXTk62Do78JfKQHaWl2ADzFWud2wZDxrs-s_YPSCooE8o'
,'https://www.colombian.com.co/vida/no-tiene-ninez-kim-kardashian-maquillo-a-su-hija-con-labial-rojo-como-una-adulta/?fbclid=IwAR2xQ57DFicROoOWVLzJ8iTzUs4wnv_tWzdJ92MU0mlHJ-iztE_8vCuY9nU'
,'https://www.colombian.com.co/judicial/encuentran-sin-vida-a-rafael-merchan-otro-testigo-clave-en-caso-de-odebrecht/?fbclid=IwAR2rWW3ew0vy6fXzUUZ1GlbxBAzx-T9Z_oKIzbC_fsZt9PONlwAKU7ujdDY'
,'https://bogotanoticias.net/2018/12/18/recaudo-de-impuestos-en-bogota-superara-los-89-billones-en-2018/?fbclid=IwAR1adZ3t4FGLlppDHU8EXg7IivajZyCKUX9sU0qoIwuAhXN1woF5O2r1Q_I'
,'https://www.pulzo.com/mundo/muere-familia-colombiana-accidente-transito-arizona-ee-uu-PP620953?fbclid=IwAR1VbPtrtR-fPUNF8hgAHv3yT8NcKlQroGcmijOlwvd08dobcqRTAi4YPuw'
,'https://www.estrending.com/entretenimiento/trending/ultima-prediccion-stephen-hawking/'
,'https://www.estrending.com/wow/personas-malhumoradas-viven-mas/?fbclid=IwAR2kz1eb0YPZhplA8Octk67Q14wqrIlbSWfOWksCtYIx6k5Iruvwe2vYgxE'
,'https://www.estrending.com/wow/los-bebes-cabezones-son-mas-inteligentes-la-ciencia-lo-confirma/'
,'https://www.pulzo.com/deportes/ayron-valle-iria-millonarios-para-alianza-lima-peru-PP620837?fbclid=IwAR3oP6jrFVv2Z_FTA42HXRakCntSdKft9RvVKp_se41Uciux682k3TqxXeQ'
,'https://www.pulzo.com/mundo/valla-uribe-miami-PP620700?fbclid=IwAR0t5GwC5vSmW9kufLc-HzpXvYr39Ojffq9DQsQhemHcfY1A8U3Kk-YM9lU'
,'https://www.pulzo.com/nacion/cargador-celular-causo-incendio-vivienda-bogota-PP620617?fbclid=IwAR2NQO0x6rcaZiC0lVNTN7r-ND3aef91BpGw9DGhhFVTJHWKBNpRmwDHVco'
,'https://www.pulzo.com/nacion/donacion-sueldo-gustavo-bolivar-PP620543?fbclid=IwAR0GbZDQIsXyqfgOWZQcqmElahiiSmnjLG9mhJhBaLfblTFC_IGSzTBdQU4'
,'https://www.pulzo.com/nacion/hallan-cianuro-cuerpo-rafael-merchan-testigo-caso-odebrecht-PP620517?fbclid=IwAR2zj3LY23yxeg2zM2S1otUJjATEIfDo1geaLkGFwAkLAp-6a4ew-NXzFUQ'
,'http://bogota.extra.com.co/noticias/judicial/procuraduria-apelo-libertad-de-guido-nule-por-no-tener-en-cu-491713?fbclid=IwAR2Ef2Od7VqjJQTiGy1r-SL7Wkzvawwuxrij4P_goiIZSWDQ7SVc-_JP5ZM'
,'http://bogota.extra.com.co/noticias/internacional/ladron-intento-robar-luchadora-de-ufc-y-termino-recibiendo-491696?fbclid=IwAR2H-1zXU7Hmj4XBLbpjWqE7SMCTm_YJNRSer6RivTdcNoIpA_f75auqQqc'
,'http://bogota.extra.com.co/noticias/internacional/brasil-se-retira-del-pacto-mundial-sobre-migracion-de-la-onu-491668?fbclid=IwAR2I1lKfjZIUJPBskCBafksG2ggqZkDWny0jUMhZc7qub546KM2fzL-7MJ0'
,'http://bogota.extra.com.co/noticias/judicial/emilio-tapia-condenado-17-anos-carrusel-de-contratacion-go-491660?fbclid=IwAR07TP_JTEuBDjWXHa42A15Dd_SveUsIWRiru6vLUT3JsueWqjnzACPaav0'
,'http://semanarioenlamira.com/sitio/odebrecht-financio-a-las-farc-por-20-anos/?fbclid=IwAR3aUxoB7QWmGVSk3PfN5cpD7ZcsgiZkjfksWgYdLpMXuRQ22iL00A4HYVQ'
,'http://elnodo.co/CUBAsamper?fbclid=IwAR1LU1VYRd_xyY6AmSXNmtAgSo61Q-PaPAGNOZUPNWRag_UBiVS15NWZLgU'
,'https://www.acontecercristiano.net/2018/05/trump-da-duro-golpe-industria-del-aborto-cancela-fondos.html?m=1&fbclid=IwAR3hFB8O7KQ8n8f75bQhplnOOb9-k7DEBvoT9CAv_uAlNAevG_M0udEtPio'
,'https://libertadusa.com/2018/11/bolsonaro-ordena-retirar-las-estatuas-del-che-guevara-en-brasil/?fbclid=IwAR06E706UK3MBwtI6KRx5mMECLkBBiMI6tYgLsreYfYsm6iuBD0dozlRnCE'
,'https://elexpediente.co/juan-manuel-santos-nobel-de-la-paz-me-secuestro-y-me-entrego-en-un-pacto-con-maduro/?fbclid=IwAR2-5LYHp-sEV9BYNFqysci9Sfzyt8FyPiRed8HKDmy6284wrRaG35W4DAA'
,'https://www.newscolombia.com.co/congreso-aprueba-2589-billones-para-presupuesto-nacional/?fbclid=IwAR0Zyl7I4m9GNWJNsEeuPeQifry2HwLGKfUejNpx4xclba0VJJrqI0mM4k0'
,'https://www.newscolombia.com.co/desde-el-congreso-proponen-restriccion-de-los-celulares-en-los-colegios/?fbclid=IwAR0tNKDbhWc4YpFqkUUGoEqmRC34uxhr07lG1qbJVUReUIvor_YYtyBtIw0'
,'https://www.newscolombia.com.co/delitos-sexuales-cometidos-por-las-farc-en-la-jep-o-en-la-justicia-ordinaria/?fbclid=IwAR09yWKh2IJd3dA5sY3llrRRi8NE-VRIpIDh8EaVJkgk-vZDL0-9xYlrtZg'
,'https://www.minuto30.com/ya-fue-radicado-el-proyecto-para-aumento-extraordinario-del-salario-minimo-que-propone-uribe/682215/?fbclid=IwAR1P0b3a86-PMcsQ_OBII21Ro-c0UjRHpeDplQ_RVmLdFjpxpK2-jZgSJvE'
,'http://paginanoticia.com/2017/10/27/confirman-que-la-marihuana-deteriora-la-capacidad-cerebral/?fbclid=IwAR3mAxZIdh5FDdGOk-QDN8rgdNcyJASjDCDbw6dXfprQD6SA6wdJEicZWes'
,'https://oiganoticias.com/2018/07/03/a-la-carcel-el-expresidente-de-ecuador-rafael-correa/?fbclid=IwAR1-NnVp3BVgE3lfMk6vBxzL0TkBqBQ7U-OxvPlT3uRFLEZ-ZeIn2CYA6xA'
]

#urlLista = 'https://www.eltiempo.com/politica/partidos-politicos/partido-liberal-apoyara-a-los-11-millones-de-la-consulta-anticorrupcion-260534'
#urlLista = "http://www.lalenguacaribe.co/petro-repitio-la-historia-de-titulos-falsos-que-tanto-critico-a-penalosa/"
#urlLista='https://www.abc.es/espana/catalunya/politica/abci-iglesias-y-junqueras-reunen-lledoners-201810191611_noticia.html'
#urlLista = 'https://cnnespanol.cnn.com/2018/11/06/este-objeto-espacial-con-forma-de-cigarrillo-podria-haber-sido-una-nave-extraterrestre-segun-astronomos-de-harvard/'
#urlLista='https://colombianoindignado.com/se-la-mando-james-con-carino-el-segundo-mandado-que-hace-duque-en-el-exterior/?fbclid=IwAR2TgpiSkboKGi0tAeendG1E0RqYVW3mO7D2Nu3GSWhuB5Y6ObZbObLvvMQ'
#urlLista = 'https://actualidadpanamericana.com/spark-vidrios-negros-completa-reten-1-000-000/?fbclid=IwAR3mHLO2DPdkQo2ELKiaqHOwA9EOI4qO1MKuFAMlH3c0MuRlNSZGsIrmY3o'
#urlLista = 'https://colombianoindignado.com/residente-dejara-subir-a-la-tarima-a-estudiantes-en-bogota-y-cali-para-apoyarlos/?fbclid=IwAR2fyjEJ1Xa_j8P2pEOvsAK1fv4ihikW0QmYJabz12NitlUqXf4kiqiQfaw'
#urlLista='http://www.zocalo.com.mx/reforma/detail/murio-belisario-betancur-a-los-95-anos'



listaFuentes = ['www.eltiempo.com',#Periodicos
                'www.elespectador.com',
                'www.elnuevosiglo.com.co',
                'www.elespaciocolombia.com',
                'www.qhubo.com',
                'www.diarioadn.co',
                'www.armada.mil.co',
                'www.publimetro.co',
                'www.larepublica.co',
                'www.portafolio.co',
                'www.elcolombiano.com',
                'www.elmundo.com',
                'www.elheraldo.co',
                'www.lalibertad.com.co',
                'www.eluniversal.com.co',
                'www.lapatria.com',
                'www.elnuevoliberal.com',
                'www.elmeridiano.co',
                'www.lanacion.com.co',
                'www.diariodelnorte.net',
                'www.elfrente.com.co',
                'www.elmeridiano.co',
                'www.elnuevodia.com.co',
                'www.elpais.com.co',
                'www.rcnradio.com',#Radio
                'www.wradio.com.co',
                'caracol.com.co',
                'www.bluradio.com',
                'www.lafm.com.co',
                'los40.com.co',
                'www.lamega.com.co',
                'cnnespanol.cnn.com',
                'www.cronicadelquindio.com',
                'www.hoy.es',#Internacionales
                'www.el-nacional.com',
                'www.24horas.cl',
                'www.df.cl',
                'mundo.sputniknews.com',
                'cnnespanol.cnn.com',
                'elpais.com',
                'www.latercera.com',
                'www.bbc.com',
                'www.abc.es',
                'www.elmundo.es',
                'www.msn.com',
                'www.lanacion.com.ar',
                'miamidiario.com',
                'www.nytimes.com',
                'www.usatoday.com',
                'www.clarin.com',
                'www.miami.com',
                'www.reforma.com',
                'www.jornada.com.mx',
                'www.eluniversal.com.mx',
                'los40.com.mx',
                'digital.elmercurio.com',
                'elmundoboston.com',
                'actualidad.rt.com',
                'www.semana.com',#Revistas
                'www.dinero.com',
                'www.enter.co',
                'www.shock.co',
                'www.teleislas.com.co',#Television
                'www.canalrcn.com',
                'www.caracoltv.com',
                'noticias.caracoltv.com',
                'noticias.canalrcn.com',
                'canal1.com.co',
                'www.canalinstitucional.tv',
                'www.ntn24.com',
                'www.cablenoticias.tv',
                'www.redmas.com.co',
                'www.canalcapital.gov.co',
                'www.teleantioquia.co',
                'www.telecaribe.co',
                'telepacifico.com',
                'noticias.canaltro.com',
                ]

def darTitulo(html):
    try:
        titulo = html.findAll('h1')
    except AttributeError as e:
        print("Error en darTitulo")
        return None
    return titulo

def darTituloAux(html):
    try:
        titulo = html.findAll('h2')
    except AttributeError as e:
        print("Error en darTituloAux")
        return None
    return titulo
def darFuente(urlLista):
    for i in range(0,len(urlLista)-len(".co/")):
        if(urlLista[i:i+len(".co/")]==".co/"):
            return urlLista[:i+len(".co/")]
    for i in range(0,len(urlLista)-len(".es/")):
        if(urlLista[i:i+len(".es/")]==".es/"):
            return urlLista[:i+len(".es/")]
    for i in range(0, len(urlLista) - len(".mx/")):
        if(urlLista[i:i + len(".mx/")] == ".mx/"):
            return urlLista[:i + len(".mx/")]
    for i in range(0,len(urlLista)-len(".ar/")):
        if(urlLista[i:i+len(".ar/")]==".ar/"):
            return urlLista[:i+len(".ar/")]
    for i in range(0,len(urlLista)-len(".cl/")):
        if(urlLista[i:i+len(".cl/")]==".cl/"):
            return urlLista[:i+len(".cl/")]
    for i in range(0,len(urlLista)-len(".com/")):
        if(urlLista[i:i+len(".com/")]==".com/"):
            return urlLista[:i+len(".com/")]
    for i in range(0,len(urlLista)-len(".org/")):
        if(urlLista[i:i+len(".org/")]==".org/"):
            return urlLista[:i+len(".org/")]
    for i in range(0,len(urlLista)-len(".gov/")):
        if(urlLista[i:i+len(".gov/")]==".gov/"):
            return urlLista[:i+len(".gov/")]
    for i in range(0,len(urlLista)-len(".net/")):
        if(urlLista[i:i+len(".net/")]==".net/"):
            return urlLista[:i+len(".net/")]
    for i in range(0, len(urlLista) - len(".tv/")):
        if (urlLista[i:i + len(".tv/")] == ".tv/"):
            return urlLista[:i + len(".tv/")]
    print("No encontre la fuente en darFuente")
    return None

def darHTML(url):
    try:
        context = ssl._create_unverified_context()
        html = urlopen(url, context=context)
        txt = html.read()
    except HTTPError as e:
        try:
            html = requests.get(url, proxies={'http': '54.39.209.39:3128'})
            txt = html.text
        except Exception as e:
            print(e)
            print("No logro abrir url en darHTML")
            print('LA URL ES: '+url)
            return None
    try:
        th = BeautifulSoup(txt,features="html.parser")
    except Exception as e:
        print("Error en darHTML")
        return None
    print('LA URL ES: ' + url)
    return th

def buscarSubString(cadena,subCadena):
    #print('subCadena: '+subCadena)
    for i in range(len(cadena) - len(subCadena)+1):
        #print('cadena: '+cadena[i:i + len(subCadena)])
        if (cadena[i:i + len(subCadena)] == subCadena):
             return subCadena,i,True
    return None,None,False

def darTexto(html):
    try:
        parr = html.findAll('p')
    except Exception as e:
        print("Error en darTexto")
        return None
    return parr

def claveTil(tituloHTML):
    #title = darTitulo(html)
    if (tituloHTML == None):
        print("no encontre el titulo en claveTil")
        return None
    else:
        tituloClave = ''
        tilClave = []
        for t in tituloHTML:
           t = t.get_text().split(' ')
           tilClave = limpiar(t)
           for pal in tilClave:
                tituloClave += pal + ' '
    return tituloClave,len(tilClave)

def claveTex(html):
    texto = darTexto(html)
    if (texto == None):
        print("no encontre el texto en claveTex")
        return None
    else:
        totalPal=0
        textoClave = ''
        for parr in texto:
            parr = limpiar(parr.get_text().split(' '))
            if(len(parr)>12):
                totalPal+=len(parr)
                for pal in parr:
                    textoClave += pal + ' '
    return textoClave,totalPal


def simbolos(letra):
    simbolos = ['/','\ '.replace(" ",""),'.', ',', ';', '"', "'", "+", "-", "_", "(", ")", "‘", "’", "<", ">",'*','“','”',"»","«",":","¿","?","!","¡"]
    for sim in simbolos:
        if(letra==sim):
            return sim
    return None

def limpiar(listaPal):
    lista = []
    sinSalto = []
    fuente = darFuente(urrl).lower()
    for pal in listaPal:
        for p in pal.splitlines():
            sinSalto.append(p)
    for pal in sinSalto:
        if (len(pal) >= 4 or pal.isdigit()):
            for letra in pal:
                cambio=simbolos(letra)
                if(cambio!=None):
                    pal=pal.replace(cambio,"")
            if(not(buscarSubString(fuente, pal.lower())[2])):
                lista.append(pal)
    return lista

def palClaveTex(titulo,texto):
    tilClave = titulo.split(' ')
    texClave = texto.split(' ')
    palTexClave =''
    i = 0
    for texPal in texClave:
        for pal in tilClave:
            if(pal==texPal):
                try:
                    antes3 = texClave[i-3]
                except IndexError as e:
                    antes3 = ''
                try:
                    antes1 = texClave[i-1]
                except IndexError as e:
                    antes1 = ''
                try:
                    antes2 = texClave[i-2]
                except IndexError as e:
                    antes2 = ''
                try:
                    despues1 = texClave[i+1]
                except IndexError as e:
                    despues1 = ''
                try:
                    despues2 = texClave[i+2]
                except IndexError as e:
                    despues2 = ''
                try:
                    despues3 = texClave[i+3]
                except IndexError as e:
                    despues3 = ''
                palTexClave += (antes2+' '+antes1+' '+despues1+' '+despues2+' ')
        i += 1
    return palTexClave

def eliminarPalRep(palClaveTodo):
    lista = palClaveTodo.split(' ')
    list=[]
    for pal in lista:
        if pal not in list:
            list.append(pal)
    return list
def busqueda(listaFinalPal):
    buscar=''
    #print(listaFinalPal)
    listaFinalPal=limpiar(listaFinalPal)
    #print(listaFinalPal)
    rango=len(listaFinalPal)

    y = 13 # siempre mayor
    if(rango>=y):
        x = 8
        for p in range(x):
            if (listaFinalPal[p] != None):
                buscar += (listaFinalPal[p] + ' ')
        for p in range(rango - (y-x), rango):
            if (listaFinalPal[p] != None):
                buscar += (listaFinalPal[p] + ' ')
    else:
        for p in range(rango):
            if (listaFinalPal[p] != None):
                buscar += (listaFinalPal[p] + ' ')

    print("buscar: "+ buscar)
    return buscar,search(buscar,tld="com.co",lang='es',num=6,start=0,stop=6,pause=1.5)

def decidir(busquedaFuente):
    confiar = []
    for f in busquedaFuente:
        for fc in listaFuentes:
            comp = buscarSubString(f, fc)[2]
            if (comp):
                confiar.append(f)
    return confiar

def resultado(decision,opcion):
    global fiables, noFiables
    if(opcion):
        if(decision):
            fiables+=1
            print("La noticia podria ser fiable, ¿que piensa usted?")
            for link in decision:
                print(link)
        else:
            noFiables+=1
            print("No encontre coincidencias, la noticia debe ser falsa")
    else:
        if (decision):
            fiables+=1
            print("¡La noticia podria ser fiable!")
        else:
            noFiables+=1
            print("¡La noticia debe ser falsa!")

#---- Grafica ------
def hacerGrafica():
    y = [fiables, noFiables]
    x = ('Fiable','No fiable')
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, width=0.3, color=['green', 'red'])
    plt.ylabel('N O T I C I A S')
    plt.xlabel('T O T A L = '+str(fiables+noFiables))
    plt.xticks(y_pos, x)
    plt.show()


for urrl in urlLista:
    html = darHTML(urrl)
    h1=darTitulo(html)
    titulo=claveTil(h1)[0]
    #print("h1: "+titulo)
    texto = claveTex(html)[0]
    palTextoClave = palClaveTex(titulo, texto)
    if (len(titulo.split(' ')) <= 5):
        titulo=texto
    #   print("sin h1: " + titulo)
        palTextoClave=''
    print("titulo: "+titulo)
    print ("palabras clave del texto: "+palTextoClave)
    decision=busqueda(eliminarPalRep(titulo+palTextoClave))
    print("sin repetir: "+decision[0])
    opcion=True
    resultado(decidir(decision[1]),opcion)
    print('\n')

hacerGrafica()
############---------
"""
def fuentesConfi(html):
    try:
        encabezado = html.find_all('h3',attrs={'class':'r'})
        links=[]
        for h3 in encabezado:
            for a in h3:
                l=str(a.attrs['href'])[7:]
                try:
                    corteL=l[:buscarSubString(l,'&')[1]]
                except TypeError as n:
                    corteL = 'No se pudo obtener link (&)'
                links.append(corteL)
        #print (links)
    except Exception as e:
        print('Error al intentar buscar fuentesConfi')
        return None
    return links

#---OTRO METODO (PERMITE OBSERVAR)----

driver = webdriver.Chrome("C:" + "\ ".replace(" ","")  + "Users\diegg\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://www.google.com.co')
element = driver.find_element_by_name("q")
element.send_keys(decision[0])
element.send_keys(Keys.RETURN)
resultado(decidir(fuentesConfi(darHTML(driver.current_url))),opcion)
#driver.close()
#driver.quit()
"""

