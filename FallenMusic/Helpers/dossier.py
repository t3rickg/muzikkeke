# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from FallenMusic import BOT_NAME

PM_START_TEXT = """
Merhaba {0}, 🥀
๏ Bu bot** {1} !

➻ Hızlı ve güçlü bir müzik oynatma botudur.
"""

START_TEXT = """
**Merhaba** {0}, 🥀
  {1} artık {2}'da şarkı çalabilir.

──────────────────
➻ Hakkımda yardım almak veya bir şey sormak isterseniz [destek sohbetime]({3}) katılabilirsiniz.
"""

HELP_TEXT = f"""
<u>❄ **{BOT_NAME} için kullanıcılar için mevcut komutlar:**</u>

๏ /oynat : İstediğiniz şarkıyı video sohbetinde çalmaya başlar.
๏ /pause : Mevcut çalan şarkıyı duraklatır.
๏ /resume : Duraklatılan şarkıyı devam ettirir.
๏ /atla : Mevcut çalan şarkıyı atlar ve sıradaki şarkıyı çalmaya başlar.
๏ /end : Sırayı temizler ve mevcut çalan şarkıyı sonlandırır.

๏ /ping : Botun ping ve sistem durumunu gösterir.
๏ /sudolist : Botun sudo kullanıcılarını gösterir.

๏ /song : İstediğiniz şarkıyı indirir ve size gönderir.

๏ /search : Verilen sorguyu YouTube'da arar ve sonuçları gösterir.
"""

HELP_SUDO = f"""
<u>✨ **{BOT_NAME} için sudo komutları:**</u>

๏ /activevc : Şu anda aktif olan sesli sohbetlerin listesini gösterir.
๏ /eval veya /sh : Verilen kodu botun terminalinde çalıştırır.
๏ /speedtest : Botun sunucusunda bir hız testi yapar.
๏ /sysstats : Botun sunucusunun sistem durumunu gösterir.

๏ /setname [metin veya bir metne yanıt] : Asistan hesabının adını değiştirir.
๏ /setbio [metin veya bir metne yanıt] : Asistan hesabının biyografisini değiştirir.
๏ /setpfp [bir fotoğrafa yanıt] : Asistan hesabının profil fotoğrafını değiştirir.
๏ /delpfp : Asistan hesabının mevcut profil fotoğrafını siler.
"""

HELP_DEV = f"""
<u>✨ **{BOT_NAME} için sahip komutları:**</u>

๏ /config : Botun tüm yapılandırma değişkenlerini alır.
๏ /broadcast [mesaj veya bir mesaja yanıt] : Botun hizmet verdiği sohbetlere mesajı yayınlar.
๏ /rmdownloads : Botun sunucusunda indirilen önbellek dosyalarını temizler.
๏ /leaveall : Asistan hesabının tüm sohbetlerden ayrılmasını sağlar.

๏ /addsudo [kullanıcı adı veya bir kullanıcıya yanıt] : Kullanıcıyı sudo kullanıcılar listesine ekler.
๏ /rmsudo [kullanıcı adı veya bir kullanıcıya yanıt] : Kullanıcıyı sudo kullanıcılar listesinden çıkarır.
"""
