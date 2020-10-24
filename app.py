from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)

class TravelingBookStack(core.Stack):
    def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        vpc = ec2.Vpc(
            self, "VPC", 
            max_azs=2,
        )

        rds.DatabaseInstance(
            self, "RDS",
            database_name="TravelingBookDB",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_12_3
            ),
            vpc=vpc,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2,
                ec2.InstanceSize.SMALL,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=False,
        ),


app = core.App()
TravelingBookStack(app, 'TravelingBookStack')
app.synth()