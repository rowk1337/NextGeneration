import discord
import asyncio
import datetime
import time
import os
import psutil as psutil

client = discord.Client()
msg_id = None
msg_user = None
COR = 0xF7FE2E

serversCount = len(client.servers) + 1

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Developped by: rowk1337#8223!"))

@client.event
async def on_member_join(member):
    nomeDoCargo ="👷 Civil 👷"
    cargo = discord.utils.get(member.server.roles, name=nomeDoCargo)
    await client.add_roles(member, cargo)
    if member.server.id == '506203112424603649':
        welcomemb = discord.Embed(color=0xF2EA00, title="Seja bem-vindo ao servidor! Por favor leia as regras!",
                              description="{}, regras: <#496388429136003092> ".format(member.mention))
        canal = client.get_channel("506218818016772106")
        welcomemb.set_image(url="https://media1.tenor.com/images/ea9df861113fecec5bb17bf1faa0124e/tenor.gif?itemid=3950966")
        welcomemb.set_footer(icon_url=member.avatar_url, text=member.name)
        await client.send_message(canal, embed=welcomemb)
    if member.server.id == '506203112424603649':
        welcomemb = discord.Embed(color=0xF2EA00, title="Bem-Vindo ao nosso servidor de discord!",
                                  description="***IP***: EM BREVE \n"
                                  "***Não esqueças de ler as regras antes de entrares no nosso servidor.*** \n"
                                  "__Diverte-te {}!__".format(member.mention))
        welcomemb.set_image(
            url="https://media1.tenor.com/images/ea9df861113fecec5bb17bf1faa0124e/tenor.gif?itemid=3950966")
        welcomemb.set_footer(icon_url=member.avatar_url, text=member.name)
        await client.send_message(member, embed=welcomemb)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!serverinfo"):
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        embed = discord.Embed(title="\n",
                                         description="Abaixo está as informaçoes principais do servidor!")
        embed.set_thumbnail(url=message.server.icon_url)
        embed.set_footer(text="{} • {}".format(message.author, horario))
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name="Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=str(len(message.server.roles)), inline=True)
        embed.add_field(name="Canais de texto:", value=str(len([c.mention for c in message.server.channels if c.type == discord.ChannelType.text])),
                                   inline=True)
        embed.add_field(name="Canais de voz:", value=str(len([c.mention for c in message.server.channels if c.type == discord.ChannelType.voice])),
                                   inline=True)
        embed.add_field(name="Membros:", value=str(len(message.server.members)), inline=True)
        embed.add_field(name="Bots:",
                                   value=str(len([a for a in message.server.members if a.bot])),
                                   inline=True)
        embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                                   inline=True)
        embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel, embed=embed)

    if message.channel == client.get_channel("506218952356265994"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    if message.channel == client.get_channel("506218253820100630"):
        await client.add_reaction(message, "✅")
        await client.add_reaction(message, "❌")

    if message.content.startswith("!ban"):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,
                                             "**Não tens permissão para executar este comando!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel,
                                      "**O usuario(a) <@{}> foi banido do servidor.**".format(user.id))
            await client.ban(user, delete_message_days=1)
        except IndexError:
            await client.send_message(message.channel, "**Você deve especificar um usuario para banir!**")
        except discord.Forbidden:
            await client.send_message(message.channel,
                                      "**Não posso banir o usuário, o cargo dele está acima do meu.**!")
        finally:
            pass

    if message.content.startswith("!ip"):
        await client.send_message(message.channel, "***__IP DO NOSSO SERVIDOR DE FIVEM__***:\n"
                                                   "37.189.193.10:30120")

    if message.content.startswith("!donators"):
        embed = discord.Embed(color=0xFFDF00, title="TOP DONATORS",
                              description="Lista dos doadores que nos ajudaram.")
        embed.set_thumbnail(url=message.server.icon_url)
        embed.add_field(name="👑 - `GOD sh0Xz*#2223`", value="40€", inline=False)
        embed.add_field(name="2 - `YvaneOficial#7966`", value="20€", inline=False)
        embed.add_field(name="2 - `@TM#3356`", value="20€", inline=False)
        embed.add_field(name="2 - `@Kelson#0984`", value="20€", inline=False)
        embed.add_field(name="3 - `@Guga#3108`", value="10€", inline=False)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/385029583696691211/2b465b31ca58fb4cb9b853a2ab6b9406.png?size=128", text="rowk1337#8223")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!denunciar'):
        await client.send_message(message.author,
                                  '**Qual úsuario você deseja denunciar {}?**'.format(message.author.mention))
        jogador = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Qual o motivo da denuncia {}?**'.format(message.author.mention))
        motivo = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Que dia aconteceu isso {}?**'.format(message.author.mention))
        dia = await client.wait_for_message(author=message.author)
        await  client.send_message(message.author, '**Tens alguma prova {}?**'.format(message.author.mention))
        prova = await client.wait_for_message(author=message.author)
        canal = client.get_channel('498186673990139904')
        embed = discord.Embed(colour=0xF0000,
                              description="O Úsuario: {} acabou de denunciar!".format(message.author.mention))
        embed.add_field(name='✏Motivo:', value=motivo.content)
        embed.add_field(name='📅Data do ocorrido:', value=dia.content)
        embed.add_field(name='🗒Prova:', value=prova.content)
        embed.add_field(name='👤Úsuario denunciado:', value=jogador.content)
        await client.send_message(canal, embed=embed)

    if message.content.lower().startswith("!anunciar"):
     msg = message.content[9:]
     if not message.author.server_permissions.administrator:
        await client.send_message(message.channel, "Você não tem permissão para executar este comando. :smile:")
        return
     if message.author.server_permissions.administrator:
        try:
            embed13 = discord.Embed(colour=COR)
            embed13.add_field(name="📢Anúncio📢", value=msg)
            embed13.set_footer(text='Publicado por: ' + message.author.name)
            embed13.set_thumbnail(url=f"{message.server.icon_url}")
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed13)
        except:
            pass

    if message.content.lower().startswith('!deletar'):
         if not message.author.server_permissions.manage_messages:
             return await client.send_message(message.channel, ":no_good: **Sem permissão!**")
         try:
             limite = int(message.content[9:]) + 1
             await client.purge_from(message.channel, limit=limite)
             msg = await client.send_message(message.channel,'{} mensagens foram deletadas com sucesso, por {}'.format(limite,
                                                                                                       message.author.mention))
             await asyncio.sleep(2)
             await client.delete_message(msg)
         except:
             await client.send_message(message.channel, ':no_good:** Sem permissão!**')

    if message.content.lower().startswith("!staff"):
        embed = discord.Embed(color=0x00ff00, title="Staff do servidor.",
                                                description="A Staff Do nosso servidor.\n\n"
                                                            "__***Fundadores:***__\n"
                                                            "Tenho de mudar mas já sabem que o rowk1337 é staff putos\n\n"
                                                            "__***Co-Fundador:***__\n"
                                                            "Tenho de mudar\n\n"
                                                            "__***Configurador:***__\n"
                                                            "Tenho de mudar\n\n"
                                                            "__***Moderador:***__\n"
                                                            "Tenho de mudar\n\n")
        embed.set_thumbnail(url=message.server.icon_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/385029583696691211/2b465b31ca58fb4cb9b853a2ab6b9406.png?size=128",text="rowk1337#8223")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!comandos'):
        user = message.author
        embed = discord.Embed(title="\n",
                              description=message.author.mention + " :mailbox_with_mail: Enviei-te os meus comandos no privado!")
        embed.add_field(name=':busts_in_silhouette: Usuário:', value=user.name)
        embed.add_field(name=':id: ID:', value=user.id)
        embed.set_footer(text="Bot criado por: rowk#8223", icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!comandos"):
        helpemb = discord.Embed(
            title="**Olá, sou o bot do servidor do Santarém RP!** \n \n",
            color=0x088A08,
            description='***COMANDOS:*** \n \n'
                        '``Informações`` \n \n'
                        ':notepad_spiral: !formulario \n \n'
                        ':book: !ip \n \n'
                        ':scroll: !staff \n \n'
                        ':money_with_wings: !donators \n \n'
                        ':chart_with_upwards_trend: !serverinfo \n \n'
                        ":robot: !botinfo"
                        "!avatar \n \n"
                        '``Administração`` \n \n'
                        ':loud_sound: !ban \n \n'
                        ':raised_hand: !mute (**EM BREVE**) \n \n'
                        ':loudspeaker: !anunciar \n \n'
                        ':x: !deletar \n \n')
        helpemb.set_image(url="https://media.giphy.com/media/39vn1E4p7XGCUWacSl/giphy.gif")
        embed.set_footer(
            icon_url="https://cdn.discordapp.com/avatars/385029583696691211/2b465b31ca58fb4cb9b853a2ab6b9406.png?size=128",
            text="rowk1337#8223")
        await client.send_message(message.author, embed=helpemb)

    if message.content.lower().startswith('!ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="Ping do bot !", color=0x2874A6,
                                   description='<a:ping:503310191098331148> `{}ms`!'.format(round((t2 - t1) * 1000)))
        ping_embed.set_footer(text="Comando enviado por {}".format(message.author),
                         icon_url="https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif")
        await client.send_message(message.channel, embed=ping_embed)

    if message.content.startswith("!avatar"):
        cor = 0x7f0000
        xtx = message.content.split(' ')
        if len(xtx) == 1:
            useravatar = message.author
            avatar = discord.Embed(
                title="Avatar de: {}".format(useravatar.name),
                color=cor,
                description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
            )

            avatar.set_image(url=useravatar.avatar_url)
            avatar.set_footer(text="Pedido por {}#{}".format(useravatar.name, useravatar.discriminator))
            await client.send_message(message.channel, embed=avatar)
        else:
            try:
                useravatar = message.mentions[0]
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=cor,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

            except IndexError:
                a = len() + 7
                uid = message.content[a:]
                useravatar = message.server.get_member(uid)
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=cor,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

    if message.content.lower().startswith('!botinfo'):
        horario = datetime.datetime.now().strftime("%H:%M")
        await client.delete_message(message)
        embedbot = discord.Embed(
            title='**Informações do Bot**',
            color=0xa4dce7,
            description='\n'
        )
        embedbot.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/385029583696691211/2b465b31ca58fb4cb9b853a2ab6b9406.png?size=128")  # Aqui você coloca a url da foto do seu bot!
        embedbot.add_field(name=':robot: | Nome', value=client.user.name, inline=True)
        embedbot.add_field(name=':id: | ID ', value=client.user.id, inline=True)
        embedbot.add_field(name='<:date:503310190758854703> | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name=':hash:  | Tag', value=client.user)
        embedbot.add_field(name=':globe_with_meridians: | Servidores', value=len(client.servers))
        embedbot.add_field(name=':family:  | Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name='‍:hammer:  | Programador', value="`rowk1337#8223 `")
        embedbot.add_field(name="<:rowkcpu:503310191299657728> | CPU Cores:",
                           value="\n\n{} cores \n".format(str(psutil.cpu_count())))
        embedbot
        embedbot.add_field(name="<:rowkcpu:503310191299657728>  | CPU Usage:",
                         value="\n\n{} % \n".format(str(psutil.cpu_percent(interval=1))))
        embedbot.add_field(name="<:rowkram:503310191379611737> | RAM Usage:",
                           value="\n\n{} % \n".format(str(psutil.virtual_memory()[2])))
        embedbot.add_field(name='<:python:503310191173828648> | Python  | Version', value="`3.6.6`")
        embedbot.add_field(name="🗺️ | Região  ", value=str(message.server.region).title(), inline=True)
        embedbot.add_field(name="💡 | Status:", value="<:online:503310191169634304> Online" )
        #message.server.get_member(client.user.id).status)
        embedbot.set_footer(
            text="Comando usado por {} Ás {}".format(message.author, horario),
            icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embedbot)

    if message.content.lower().startswith('!bonus'):
        await client.delete_message(message)
        embedbot = discord.Embed(
            title='**Bónus ao ajudares o servidor**',
            color=0xa4dce7,
            description='\n'
        )
        embedbot.set_thumbnail(url=message.server.icon_url)  # Aqui você coloca a url da foto do seu bot!
        embedbot.add_field(name='5€', value="500.000€ no servidor", inline=False)
        embedbot.add_field(name='10€', value="1.000.000€ no servidor", inline=False)
        embedbot.add_field(name='15€', value="1.500.000€ no servidor", inline=False)
        embedbot.add_field(name='20€', value="3.000.000€ no servidor + 1 vehículo da concessionaria", inline=False)
        embedbot.add_field(name='30€', value="5.500.000€ no servidor + 2 vehículos da concessionaria", inline=False)
        embedbot.add_field(name='40€', value="7.000.000€ no servidor + 1 casa a escolha + 2 vehículos da concessionaria \n( ou 7.000.000€ + 1 carro exclusivo + uma casa )", inline=False)
        embedbot.add_field(name='50€', value="10.000.000€ no servidor + 2 vehículos da concessionaria + vehículo exclusivo + 2 casas", inline=False)
        embedbot.add_field(name="\n\n Para mais informações:", value="Falar com o `no lo se`", inline=False)
        embedbot.set_footer(text="Next Generation RP",icon_url="https://cdn.discordapp.com/avatars/430457464949964800/b793d694b3927329b4f4b4564ec87a81.webp?size=1024")
        await client.send_message(message.channel, embed=embedbot)

    if message.content.lower().startswith('!metodos'):
        await client.delete_message(message)
        embedbot = discord.Embed(title='**Métodos de pagamento**',color=0xa4dce7, description='\n')
        embedbot.add_field(name='Lista:', value="Paypal \n PaySafeCard \n`)", inline=False)
        embedbot.set_thumbnail(url=message.server.icon_url)
        embedbot.set_footer(text="Next Generation RP",icon_url="https://cdn.discordapp.com/avatars/430457464949964800/b793d694b3927329b4f4b4564ec87a81.webp?size=1024")
        await client.send_message(message.channel, embed=embedbot)

    if message.content.startswith('!candidatarparamecanico'):
        Embed = discord.Embed(color=0xFFA500, description='**📬 Faça o formulario para mecanico no `privado`!**')
        await message.channel.send(embed=Embed)
        await message.author.send('** `Qual é o teu nome?`**'.format(message.author.mention))
        nome = await message.author.wait_for_message()
        await message.author.send('**🗣 `Que Idade tens?`**'.format(message.author.mention))
        idade = await message.author.wait_for_message()
        await message.author.send('**📆 `Quanto tempo tens diariamente para jogar no servidor?`**'.format(message.author.mention))
        tempo = await message.author.wait_for_message()
        await message.author.send('**🌎 `O que entendes pelo emprego Mecânico?`**'.format(message.author.mention))
        mecanico = await message.author.wait_for_message()
        await message.author.send('**📠 `Conheces bem as regras do servidor? !`**'.format(message.author.mention))
        regras = await message.author.wait_for_message()
        await message.author.send('**🔊 `Há quanto tempo jogas no servidor?`**'.format(message.author.mention))
        tempo2 = await message.author.wait_for_message()
        await message.authort.send('**🔔 `Qual é a tua experiência em roleplay? Dá-nos também um exemplo de Roleplay entre duas pessoas, dentro deste emprego, utilizando os comandos /me?"`**'.format(message.author.mention))
        experienca = await message.author.wait_for_message()
        await message.author.send('**📠 `Queres dizer mais alguma merda filho da puta?`**'.format(message.author.mention))
        terminado = await message.author.wait_for_message()
        canal = client.get_channel('506223594624385024')
        embed = discord.Embed(colour=0xF0000,
                              description="O usuário : {} acabou de se candidatar para Mecanico FODASE GANDA MECANICO!".format(message.author.mention))
        embed.add_field(name='Nome:', value=nome.content)
        embed.add_field(name='Idade:', value=idade.content)
        embed.add_field(name='Tempo diario:', value=tempo.content)
        embed.add_field(name='Oque o usuario entende pelo emprego mecanico:', value=mecanico.content)
        embed.add_field(name='Ele conheçe as regras:', value=regras.content)
        embed.add_field(name='Há quanto tempo ele joga:', value=tempo2.content)
        embed.add_field(name='Se o rapaz tem experiença em roleplay:', value=experienca.content)
        embed.add_field(name='Outros:', value=terminado.content)
        await client.send_message(canal, embed=embed)
        
client.run(os.getenv('TOKEN'))
