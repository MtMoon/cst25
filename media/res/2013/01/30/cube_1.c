#include <stdlib.h>
#include <GL/glut.h>

char cube[7][3][3];
int e[4][3][2]={
    0,0,1,0,2,0,
    2,0,2,1,2,2,
    2,2,1,2,0,2,
    0,2,0,1,0,0};

void replace(int f2,int e2,int f1,int e1,int r){
    if(r==0){
        for(int i=0;i<3;i++){
            cube[f1][e[e1][i][0]][e[e1][i][1]]=cube[f2][e[e2][i][0]][e[e2][i][1]];
        }
    }else{
        for(int i=0;i<3;i++){
            cube[f1][e[e1][2-i][0]][e[e1][2-i][1]]=cube[f2][e[e2][i][0]][e[e2][i][1]];
        }
    }
}

void clockwise(int f){
    int t1=cube[f][0][0];
    int t2=cube[f][0][1];
    cube[f][0][0]=cube[f][2][0];
    cube[f][2][0]=cube[f][2][2];
    cube[f][2][2]=cube[f][0][2];
    cube[f][0][2]=t1;
    cube[f][0][1]=cube[f][1][0];
    cube[f][1][0]=cube[f][2][1];
    cube[f][2][1]=cube[f][1][2];
    cube[f][1][2]=t2;
    
}

void aclockwise(int f){
    clockwise(f);
    clockwise(f);
    clockwise(f);
}

#define F 0
#define B 1
#define L 2
#define R 3
#define U 4
#define D 5

void tF(){
    clockwise(F);
    replace(U,1,6,0,0);
    replace(L,2,U,1,0);
    replace(D,3,L,2,0);
    replace(R,0,D,3,0);
    replace(6,0,R,0,0);
}

void tB(){
    clockwise(B);
    replace(U,3,6,0,0);
    replace(R,2,U,3,0);
    replace(D,1,R,2,0);
    replace(L,0,D,1,0);
    replace(6,0,L,0,0);
}

void tL(){
    clockwise(L);
    replace(U,0,6,0,0);
    replace(B,2,U,0,0);
    replace(D,0,B,2,0);
    replace(F,0,D,0,0);
    replace(6,0,F,0,0);
}

void tR(){
    clockwise(R);
    replace(U,2,6,0,0);
    replace(F,2,U,2,0);
    replace(D,2,F,2,0);
    replace(B,0,D,2,0);
    replace(6,0,B,0,0);
}

void tU(){
    clockwise(U);
    replace(F,3,6,0,0);
    replace(R,3,F,3,0);
    replace(B,3,R,3,0);
    replace(L,3,B,3,0);
    replace(6,0,L,3,0);
}

void tD(){
    clockwise(D);
    replace(F,1,6,0,0);
    replace(L,1,F,1,0);
    replace(B,1,L,1,0);
    replace(R,1,B,1,0);
    replace(6,0,R,1,0);
}
    
void tFi(){tF();tF();tF();}    
void tBi(){tB();tB();tB();}    
void tLi(){tL();tL();tL();}    
void tRi(){tR();tR();tR();}    
void tUi(){tU();tU();tU();}    
void tDi(){tD();tD();tD();}

void drawFacet(int facet, int color, int offset[])
{
    int i;
    glBegin(GL_POLYGON);
    glColor3fv(colorMap[color]);
    for(i = 0; i < 4; i++)
	glVertex3f(facetMap[facet][i][0]+offset[0],
		   facetMap[facet][i][1]+offset[1],
		   facetMap[facet][i][2]+offset[2]);
    glEnd();
}

void drawBlock(block_t *block)
{
    int i;
    for(i = 0; i < 6; i++) 
	/* Draw Facet i */
	drawFacet(i, block.color[i], block.offset);
}

void drawSlice(int facet, int axis)
{
    int i;
    block_t *blocks = sequence[axis][facet];
    for(i = 0; i < 9; i++)
	drawBlock(blocks++);
}

void drawCube()
{
    if(spinFacet == -1) {
	drawSlice(0,1);
	drawSlice(1,1);
	drawSlice(2,1);
    } else {
	glPushMatrix();
	applySpin();
	drawSlice(spinMap[spinFacet][1], spinMap[spinFacet][0]);
	glPopMatrix();
	drawSlice(spinMap[spinFacet][2], spinMap[spinFacet][0]);
	drawSlice(spinMap[spinFacet][3], spinMap[spinFacet][0]);
    }
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    /* Draw Functions */
    drawCube();
    
    glFlush();
    glutSwapBuffers();
}

void spinCube()
{
    if(spinFacet != -1) {
	theta += 5.0 * spinDir;
	if(theta > 90.0) {
	    spinFacet = -1;
	    spinFunc();
	}
    }
    if(spinFacet == -1) {
	spinFacet = spinSeq[nextSpin].facet;
	spinDir = spinSeq[nextSpin].dir;
	spinFunc = spinSeq[nextSpin].func;
	nextSpin++;
	theta = 0;
    }
    glutPostRedisplay();
}


void myReshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if(w <= h)
	glOrtho(-6.0, 6.0, -6.0 * (GLfloat)h / (GLfloat)w,
		6.0 * (GLfloat)h / (GLfloat)w, -10.0, 10.0);
    else
	glOrtho(-6.0 * (GLfloat)w / (GLfloat)h, 6.0 * (GLfloat)w / (GLfloat)h,
		-6.0, 6.0, -10.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutCreateWindow("CUBE");
    glutReshapeFunc(myReshape);
    glutDisplayFunc(display);
    glutIdleFunc(spinCube);
    glEnable(GL_DEPTH_TEST);
    glutMainLoop();
}
   
   
