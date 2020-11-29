GL_VERTEX_NATIVE_SHADER = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texcoords;
uniform mat4 theMatrix;
uniform vec3 GL_LIGHT_USAGE;
uniform float time;
out float intensity;
out vec2 vertexTexcoords;
out vec3 v3Position;
out vec3 fnormal;
out float timer;
void main()
{
	fnormal = normal;
	vertexTexcoords = texcoords;
	v3Position = position;
	timer = time;
	intensity = dot(normal, normalize(GL_LIGHT_USAGE));
	gl_Position = theMatrix * vec4(position.x, position.y, position.z, 1.0);
}
"""

GL_VERTEX_NATIVE_FRAGMENT = """
#version 460
layout(location = 0) out vec4 fragColor;
in float intensity;
in vec2 vertexTexcoords;
uniform sampler2D tex;
uniform vec4 GL_DIFFUSE_USAGE;
uniform vec4 GL_AMBIENT;
void main()
{
	fragColor = texture(tex, vertexTexcoords);
}
"""

#Lineas verticales que lo atraviezan
GL_SCANNER_FIRST_HALO = """
#version 460
layout(location = 0) out vec4 fragColor;
in float intensity;
in vec2 vertexTexcoords;
in vec3 v3Position;
in float timer;
uniform sampler2D tex;
uniform vec4 GL_DIFFUSE_USAGE;
uniform vec4 GL_AMBIENT;
void main()
{
	float time = timer/0.2;
	float bright =  floor(mod(v3Position.x+timer, time)*2.5) + floor(mod(v3Position.z*5.0, 1.0));
  vec4 color = mod(bright, 2.0) > .5 ? vec4(2.0, .0, 0.0, 1.0) : vec4(0.0, 3.0, 1.0, 1.0);
  fragColor = color * intensity;
}
"""

#este se miraba mas chilero en el mono 
#este cambia de azul a amarillo 
GL_SCANNER = """
#version 460
layout(location = 0) out vec4 fragColor;
in float intensity;
in vec2 vertexTexcoords;
in vec3 v3Position;
in float timer;
uniform sampler2D tex;
uniform vec4 GL_DIFFUSE_USAGE;
uniform vec4 GL_AMBIENT;
void main()
{
	float time = timer/0.3f;
	if (time > 1.0 ) 
	{
		time = time * 2.0f;
	}
	else if (timer > 10) 
	{
		time = time / 100.0f;
	}
	else 
	{
		time = timer /2.2f;
	}

	float bright = floor(mod(v3Position.z*time, 1.0)+timer);
  vec4 color = mod(bright, 2.0) > .8 ? vec4(1.0, 3.0, 1.0, .5) : vec4(1.0, 1.0, 1.0, 1.0);
  fragColor = color * intensity;
}
"""

GL_PARTAY = """
#version 460
layout (location = 0) out vec4 fragColor;

in float intensity;
in vec2 vertexTexcoords;
in vec3 v3Position;
in float timer;

uniform sampler2D tex;
uniform vec4 GL_DIFFUSE_USAGE;
uniform vec4 GL_AMBIENT;

void main()
{
	float given_time = timer/0.2;
	float red = mod(timer * 128, 10);
	float blue = mod(timer * 35, 10);
	float green = mod(timer * 515, 10);
	float bright = floor(mod(v3Position.z * given_time, 1.0) + timer);
	vec4 color = mod(bright, 3.0) > 1 ? vec4(red, blue, green, 1.0) : vec4(blue, green, red, 1.0);
	fragColor = color * intensity;
}
"""


GL_NORMALS = """
#version 460
layout(location = 0) out vec4 fragColor;
in float intensity;
in vec2 vertexTexcoords;
in vec3 fnormal;
uniform sampler2D tex;
uniform vec4 GL_DIFFUSE_USAGE;
uniform vec4 GL_AMBIENT;
void main()
{
	fragColor = vec4(fnormal, 1.1);
}
"""