from unittest import TestCase
from src.core.parser import find_spreadsheet_link_from_html


def get_html_content():
    return r"""<section class="texto">
                  <div class="container">
                    <div class="row">
                      <div class="col-12">
                
                        <h1><strong><span style="color: #008000;">SAIBA SOBRE AS INTERRUPÇÕES PROGRAMADAS DE ENERGIA NA SUA
                              REGIÃO</span></strong></h1>
                        <p>A Cemig realiza interrupções no fornecimento da energia elétrica para realização de obras de melhoria e de
                          manutenção na rede elétrica para garantir maior confiabilidade do fornecimento de energia,</p>
                        <p>Para sua maior comodidade, você pode receber avisos de desligamentos em sua região por SMS ou e-mail, basta
                          atualizar os seus dados no<a href="https://atende.cemig.com.br/AtualizarMeiosContato"><strong><span
                                style="color: #ff6600;"> Cemig Atende Web</span></strong></a>. <strong><span
                              style="color: #008000;">Saiba mais</span></strong> <a
                            href="https://www.cemig.com.br/noticia/interrupcoes-programadas-saiba-como-receber-informes-sobre-manutencoes-na-rede-eletrica/"><strong><span
                                style="color: #ff6600;">aqui</span></strong></a>.</p>
                        <p>&gt; Caso ocorra algum fato que impeça a realização dos serviços, essa interrupção poderá ser cancelada sem
                          aviso prévio.</p>
                        <p>&gt; Por medida de segurança, considere sempre a rede da Cemig energizada, mesmo durante a manutenção.</p>
                        <h4><a href="https://www.cemig.com.br/wp-content/uploads/2023/06/desligamentos-programados.xls" target="_blank"
                            rel="noopener"><strong><span style="color: #ff6600;">Confira aqui a programação de desligamentos programados
                                para os próximos dias</span></strong></a></h4>
                        <p>&nbsp;</p>
                        <p>&nbsp;</p>
                
                      </div>
                    </div>
                  </div>
                </section>"""


def get_expected_result():
    return r"""[<a href="https://www.cemig.com.br/wp-content/uploads/2023/06/desligamentos-programados.xls" rel="noopener" target="_blank"><strong><span style="color: #ff6600;">Confira aqui a programação de desligamentos programados
                                para os próximos dias</span></strong></a>]"""


class Test(TestCase):

    def test_find_spreadsheet_link_from_html(self):
        """When a html content is provided as string,
           then return the required link from it"""
        content = find_spreadsheet_link_from_html(get_html_content())
        self.assertIsInstance(content, list)
        self.assertTrue(len(content) > 0)
        self.assertEqual(str(content), get_expected_result())

