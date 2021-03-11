import discord

client=discord.Client(intents=discord.Intents.all())

activityA=discord.Activity(type=discord.ActivityType.playing, name='?help')
@client.event
async def on_ready():
  print('I have logged in!')
  await client.change_presence(activity=activityA, status=discord.Status.dnd)


prefixEmbed=discord.Embed(title='Bots Prefix', color=discord.Colour.from_rgb(0, 255, 0), description='**ProBot ✨#5803** - !\n- - - - - - - -\n**Groovy#7254** - /\n- - - - - - - -\n**The Safe House#7796** - ;\n- - - - - - - -\n**Arcane#7800** - #\n- - - - - - - -\n**TweetShift#4434** - >')
helpEmbed=discord.Embed(title='Greetings, I am TestAssistant.', color=discord.Colour.from_rgb(0, 255, 157), description='Hello there, I am TestAssistant. I am a bot made for testing functionalities that is having in discord.py. I am also being used for minor functions that other bots in the server may not have. Anything about me can contact to HMgamingSecondary#7886 or HMgamingTertiary#3464. Here are my commands:')

prefix='?'
helpEmbed.add_field(name='{}botPrefix'.format(prefix), value='List out prefixes of all bots in the server.')
@client.event
async def on_message(message):
  msg=message
  chann=msg.channel
  if msg.author==client.user:
    return
  if chann.type==discord.ChannelType.private or chann.type==discord.ChannelType.group:
    return
  if msg.content.startswith(prefix+'botPrefix'):
    prefixEmbed.set_footer(text='TestAssistant by HMgamingSecondary#7886', icon_url=client.user.avatar_url)
    await chann.send(embed=prefixEmbed)
  if msg.content.startswith(prefix+'help'):
    helpEmbed.set_footer(text='TestAssistant by HMgamingSecondary#7886', icon_url=client.user.avatar_url)
    await chann.send(embed=helpEmbed)
  if msg.content.startswith(prefix+'leaveMessageChannel'):
    if msg.author.id==704862713695961210 or msg.author.id==795296008761901086:
      channelID=msg.content.split(prefix+'leaveMessageChannel ', 1)[1]
      try:
        channelID=int(channelID)
      except:
        await chann.send(':x: The channel ID is not a number!')
        return
      givenChannel=msg.guild.get_channel(channelID)
      if not givenChannel==None:
        if givenChannel.type==discord.ChannelType.text:
          idFile=open('greetChannelId/{}'.format(msg.guild.id), 'w')
          idFile.write(str(channelID))
          idFile.close()
          await chann.send(':white_check_mark: Success!')
    else:
      await chann.send('only hmgaming allow nerd.')
    
@client.event
async def on_member_remove(memb):
  guild=memb.guild
  if guild.get_member(memb.id)==None:
    idFile=open('greetChannelId/{}'.format(guild.id), 'r')
    givenId=int(idFile.read())
    idFile.close()
    givenChannel=guild.get_channel(givenId)
    if not givenChannel==None:
      await givenChannel.send('{} left the server, hope you have a fun time! :wave:'.format(memb.mention))
   
client.run() 
